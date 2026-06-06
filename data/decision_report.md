# Decision Report

- generated_at: 2026-06-06T10:39:56.044062+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5810**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5810, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 8/20 | 40.0% | +2.23% | **+0.89%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.40% | **+0.18%** |
| LIMIT_6PCT | 4/20 | 20.0% | +0.42% | **+0.08%** |
| LIMIT_ATR | 17/20 | 85.0% | -0.23% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.59% | **+1.59%** |
| MARKET_LONG | 20/20 | 100.0% | +1.40% | **+1.40%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.82% | **+1.37%** |
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +1.05% | **+1.05%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +2.97% | **+0.89%** |

## 2. $100 Live Portfolio

- 残高: **$100.00** / 初期 $100.00 (+0.00%)
- 確定トレード: 0件 (TP 0 / SL 0 / EXP 0)

## 3. Safe Adaptive DryRun ($100)

- 残高: **$130.54** / 初期 $100.00 (+30.54%)
- 確定: 1013件 (Win 239 / Loss 313 / Flat 461) / skip 1358件
- 成長率目線: 平均log +0.000263 / 幾何平均 +0.026% per trade / maxDD +7.25%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HOME/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $130.54

## 4. Latest Market Context

- 更新: 2026-06-06T10:39:52.055636+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -1.14% price=60259.1
- Funnel: target 771 → liquid 151 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.6 >= 65=1, 4h RSI 85.0 >= 65=1, 4h RSI 81.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ALLO/USDT:USDT | +82.68% | $26,605,196.89 |
| BLUAI/USDT:USDT | +59.09% | $2,494,664.63 |
| VELVET/USDT:USDT | +39.55% | $2,896,847.12 |
| HEI/USDT:USDT | +32.48% | $2,457,536.32 |
| CLO/USDT:USDT | +19.73% | $2,611,689.12 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VELVET/USDT:USDT | below_1h_threshold | +3.84% | +4.99% |
| HOME/USDT:USDT | below_1h_threshold | +3.76% | +4.90% |
| EPIC/USDT:USDT | below_1h_threshold | +1.87% | +3.01% |
| SKYAI/USDT:USDT | below_1h_threshold | +0.99% | +2.14% |
| LYN/USDT:USDT | below_1h_threshold | +0.17% | +1.31% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
