# Decision Report

- generated_at: 2026-05-12T07:52:58.722054+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4100**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4100, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=-1.78%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.78% | **-1.78%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |
| LIMIT_FIB1272 | 3/20 | 15.0% | +3.23% | **+0.48%** |
| LIMIT_5PCT | 6/20 | 30.0% | +1.30% | **+0.39%** |
| LIMIT_4PCT | 15/20 | 75.0% | -0.27% | **-0.20%** |
| LIMIT_ATR | 18/20 | 90.0% | -0.61% | **-0.55%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +3.23% | **+2.42%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +3.91% | **+2.15%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +2.83% | **+1.84%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.74% | **+1.57%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +2.80% | **+1.12%** |

## 2. $100 Live Portfolio

- 残高: **$99.19** / 初期 $100.00 (-0.81%)
- 確定トレード: 34件 (TP 9 / SL 22 / EXP 3)
- 最新: DOGS/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.19
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$112.33** / 初期 $100.00 (+12.33%)
- 確定: 236件 (Win 62 / Loss 81 / Flat 93) / skip 425件
- 成長率目線: 平均log +0.000493 / 幾何平均 +0.049% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SAGA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.77% 残高後 $112.33

## 4. Latest Market Context

- 更新: 2026-05-12T07:52:55.133935+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=80891.2
- Funnel: target 762 → liquid 192 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.5 >= 65=1, 4h RSI 88.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| GIGA/USDT:USDT | +50.39% | $3,318,730.50 |
| SAGA/USDT:USDT | +47.44% | $10,605,445.57 |
| SKYAI/USDT:USDT | +35.93% | $43,630,611.30 |
| USELESS/USDT:USDT | +31.89% | $6,084,345.22 |
| SAPIEN/USDT:USDT | +27.18% | $1,087,691.11 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIOT/USDT:USDT | below_1h_threshold | +4.86% | +4.98% |
| SAHARA/USDT:USDT | below_1h_threshold | +4.69% | +4.82% |
| RIF/USDT:USDT | below_1h_threshold | +4.03% | +4.15% |
| GIGA/USDT:USDT | below_1h_threshold | +3.82% | +3.94% |
| USELESS/USDT:USDT | below_1h_threshold | +2.88% | +3.00% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
