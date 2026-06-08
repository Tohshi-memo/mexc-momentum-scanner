# Decision Report

- generated_at: 2026-06-08T21:15:07.001311+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6097**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6097, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-2.21%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.21% | **-2.21%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +2.91% | **+0.87%** |
| LIMIT_5PCT | 10/20 | 50.0% | +1.66% | **+0.83%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.57% | **+0.40%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.55% | **+0.22%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 8/20 | 40.0% | +3.06% | **+1.23%** |
| MARKET_LONG | 20/20 | 100.0% | +1.12% | **+1.12%** |
| LIMIT_BB3S_LONG | 4/7 | 57.1% | +1.87% | **+1.07%** |
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +1.65% | **+1.07%** |
| LIMIT_6PCT_LONG | 4/20 | 20.0% | +5.00% | **+1.00%** |

## 2. $100 Live Portfolio

- 残高: **$97.59** / 初期 $100.00 (-2.41%)
- 確定トレード: 9件 (TP 1 / SL 7 / EXP 1)
- 最新: SKYAI/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.59
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$151.21** / 初期 $100.00 (+51.21%)
- 確定: 1144件 (Win 280 / Loss 350 / Flat 514) / skip 1514件
- 成長率目線: 平均log +0.000361 / 幾何平均 +0.036% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GUA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $151.21

## 4. Latest Market Context

- 更新: 2026-06-08T21:15:04.027010+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.39% price=63703.9
- Funnel: target 777 → liquid 150 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +20.63% | $20,945,004.50 |
| PIPPIN/USDT:USDT | +17.78% | $29,619,716.07 |
| WLD/USDT:USDT | +16.17% | $115,072,393.94 |
| LAYER/USDT:USDT | +13.45% | $1,838,670.46 |
| B/USDT:USDT | +9.45% | $1,856,341.10 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NIGHT/USDT:USDT | below_1h_threshold | +2.17% | +1.79% |
| FOLKS/USDT:USDT | below_1h_threshold | +1.99% | +1.60% |
| SNT/USDT:USDT | below_1h_threshold | +1.62% | +1.24% |
| WLD/USDT:USDT | below_1h_threshold | +1.56% | +1.18% |
| ZEC/USDT:USDT | below_1h_threshold | +1.47% | +1.08% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
