# Decision Report

- generated_at: 2026-05-09T01:52:38.872254+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3835**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3835, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=-2.33%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.33% | **-2.33%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 11/20 | 55.0% | +0.74% | **+0.41%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_BB3S | 5/15 | 33.3% | +0.47% | **+0.16%** |
| LIMIT_4PCT | 16/20 | 80.0% | +0.02% | **+0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +2.61% | **+1.96%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +3.59% | **+1.62%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +3.85% | **+1.54%** |
| LIMIT_5PCT_LONG | 7/20 | 35.0% | +3.83% | **+1.34%** |
| ASK_LONG | 20/20 | 100.0% | +1.33% | **+1.33%** |

## 2. $100 Live Portfolio

- 残高: **$98.33** / 初期 $100.00 (-1.67%)
- 確定トレード: 28件 (TP 7 / SL 19 / EXP 2)
- 最新: IO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.33
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 193件 (Win 48 / Loss 64 / Flat 81) / skip 203件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +3.48%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BILL/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-09T01:52:34.917617+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.24% price=80382.1
- Funnel: target 767 → liquid 178 → pre 50 → checked 50 → surge 4 → strict 1
- Surge前reject: below_1h_threshold=45, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 74.0 >= 65=1, 4h RSI 81.1 >= 65=1, 4h RSI 72.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ICP/USDT:USDT | +27.85% | $234,846,522.05 |
| AGT/USDT:USDT | +23.33% | $6,649,247.83 |
| COLLECT/USDT:USDT | +20.22% | $6,691,133.87 |
| DEEP/USDT:USDT | +19.06% | $1,150,473.31 |
| CORE/USDT:USDT | +16.51% | $1,789,010.00 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PYTH/USDT:USDT | below_relative_strength | +5.18% | +4.95% |
| IP/USDT:USDT | below_1h_threshold | +3.34% | +3.10% |
| SPK/USDT:USDT | below_1h_threshold | +3.03% | +2.79% |
| CORE/USDT:USDT | below_1h_threshold | +2.97% | +2.73% |
| GIGGLE/USDT:USDT | below_1h_threshold | +2.93% | +2.70% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
