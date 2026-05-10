# Decision Report

- generated_at: 2026-05-10T18:47:42.988152+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3982**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3982, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=-0.86%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.86% | **-0.86%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.42% | **+0.19%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.05% | **+0.03%** |
| LIMIT_BB3S | 4/14 | 28.6% | -0.80% | **-0.23%** |
| LIMIT_3PCT | 14/20 | 70.0% | -0.44% | **-0.31%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.36% | **+1.08%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.43% | **+0.93%** |
| MARKET_LONG | 20/20 | 100.0% | +0.85% | **+0.85%** |
| ASK_LONG | 20/20 | 100.0% | +0.82% | **+0.82%** |
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +0.79% | **+0.64%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 30件 (TP 7 / SL 20 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$107.73** / 初期 $100.00 (+7.73%)
- 確定: 198件 (Win 48 / Loss 66 / Flat 84) / skip 345件
- 成長率目線: 平均log +0.000376 / 幾何平均 +0.038% per trade / maxDD +4.09%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BILL/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $107.73

## 4. Latest Market Context

- 更新: 2026-05-10T18:47:39.535961+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.27% price=81226.5
- Funnel: target 769 → liquid 167 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 91.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ALCH/USDT:USDT | +20.71% | $2,063,709.46 |
| TRUTH/USDT:USDT | +14.22% | $2,252,587.49 |
| DEEP/USDT:USDT | +13.70% | $1,606,533.93 |
| B/USDT:USDT | +13.58% | $1,824,494.09 |
| SUI/USDT:USDT | +11.24% | $544,835,823.63 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SAHARA/USDT:USDT | below_1h_threshold | +4.03% | +4.30% |
| SEI/USDT:USDT | below_1h_threshold | +3.91% | +4.17% |
| ALCH/USDT:USDT | below_1h_threshold | +3.63% | +3.89% |
| DEEP/USDT:USDT | below_1h_threshold | +3.58% | +3.85% |
| 1000BONK/USDT:USDT | below_1h_threshold | +3.54% | +3.81% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
