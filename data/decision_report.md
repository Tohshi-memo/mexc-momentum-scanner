# Decision Report

- generated_at: 2026-06-08T23:00:25.172723+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6101**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6101, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.26%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.26% | **-1.26%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 13/20 | 65.0% | +1.04% | **+0.68%** |
| LIMIT_5PCT | 10/20 | 50.0% | +1.16% | **+0.58%** |
| LIMIT_6PCT | 6/20 | 30.0% | +1.92% | **+0.58%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.62% | **+0.25%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 5/20 | 25.0% | +3.78% | **+0.95%** |
| LIMIT_6PCT_LONG | 5/20 | 25.0% | +3.57% | **+0.89%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +1.74% | **+0.87%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +2.08% | **+0.73%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +3.27% | **+0.65%** |

## 2. $100 Live Portfolio

- 残高: **$97.59** / 初期 $100.00 (-2.41%)
- 確定トレード: 9件 (TP 1 / SL 7 / EXP 1)
- 最新: SKYAI/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.59
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$151.21** / 初期 $100.00 (+51.21%)
- 確定: 1144件 (Win 280 / Loss 350 / Flat 514) / skip 1518件
- 成長率目線: 平均log +0.000361 / 幾何平均 +0.036% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GUA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $151.21

## 4. Latest Market Context

- 更新: 2026-06-08T23:00:22.630936+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.00% price=63404.9
- Funnel: target 777 → liquid 152 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +33.63% | $22,475,699.72 |
| 4/USDT:USDT | +22.59% | $1,183,086.96 |
| PIPPIN/USDT:USDT | +14.66% | $30,645,055.18 |
| LAYER/USDT:USDT | +14.32% | $2,064,516.95 |
| BLESS/USDT:USDT | +9.29% | $9,338,909.81 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BLESS/USDT:USDT | below_1h_threshold | +0.27% | +0.27% |
| WLFI/USDT:USDT | below_1h_threshold | +0.22% | +0.23% |
| FOLKS/USDT:USDT | below_1h_threshold | +0.17% | +0.17% |
| WLD/USDT:USDT | below_1h_threshold | +0.16% | +0.17% |
| B/USDT:USDT | below_1h_threshold | +0.10% | +0.10% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
