# Decision Report

- generated_at: 2026-05-09T01:47:44.819835+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3834**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3834, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=-2.33%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.33% | **-2.33%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 9/20 | 45.0% | +0.95% | **+0.43%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_FIB1272 | 11/20 | 55.0% | +0.63% | **+0.35%** |
| LIMIT_BB3S | 5/16 | 31.2% | +0.47% | **+0.15%** |
| LIMIT_4PCT | 16/20 | 80.0% | +0.02% | **+0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +2.61% | **+2.61%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +4.03% | **+2.02%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +2.38% | **+1.54%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +3.85% | **+1.54%** |
| LIMIT_5PCT_LONG | 7/20 | 35.0% | +3.83% | **+1.34%** |

## 2. $100 Live Portfolio

- 残高: **$98.33** / 初期 $100.00 (-1.67%)
- 確定トレード: 28件 (TP 7 / SL 19 / EXP 2)
- 最新: IO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.33
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 193件 (Win 48 / Loss 64 / Flat 81) / skip 202件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +3.48%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BILL/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-09T01:47:41.225217+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.17% price=80331.7
- Funnel: target 767 → liquid 177 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=46, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.0 >= 65=1, 4h RSI 79.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| COLLECT/USDT:USDT | +25.96% | $6,661,985.24 |
| ICP/USDT:USDT | +25.00% | $233,868,242.38 |
| DEEP/USDT:USDT | +19.21% | $1,140,928.63 |
| AGT/USDT:USDT | +19.18% | $6,582,734.65 |
| CORE/USDT:USDT | +18.21% | $1,778,327.22 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SIREN/USDT:USDT | below_relative_strength | +5.02% | +4.85% |
| CORE/USDT:USDT | below_1h_threshold | +4.41% | +4.23% |
| IP/USDT:USDT | below_1h_threshold | +3.34% | +3.17% |
| PYTH/USDT:USDT | below_1h_threshold | +3.21% | +3.04% |
| SPK/USDT:USDT | below_1h_threshold | +2.95% | +2.78% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
