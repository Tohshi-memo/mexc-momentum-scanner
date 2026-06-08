# Decision Report

- generated_at: 2026-06-08T16:12:42.182162+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6083**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6083, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.93%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.93% | **-0.93%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +0.33% | **+0.13%** |
| LIMIT_6PCT | 3/20 | 15.0% | -0.08% | **-0.01%** |
| LIMIT_7PCT | 2/20 | 10.0% | -0.60% | **-0.06%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | -0.26% | **-0.09%** |
| LIMIT_4PCT | 14/20 | 70.0% | -0.29% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.13% | **+1.13%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +1.17% | **+0.82%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +1.56% | **+0.78%** |
| ASK_LONG | 20/20 | 100.0% | +0.68% | **+0.68%** |
| LIMIT_2PCT_LONG | 9/20 | 45.0% | +0.92% | **+0.41%** |

## 2. $100 Live Portfolio

- 残高: **$97.59** / 初期 $100.00 (-2.41%)
- 確定トレード: 9件 (TP 1 / SL 7 / EXP 1)
- 最新: SKYAI/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.59
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$151.21** / 初期 $100.00 (+51.21%)
- 確定: 1144件 (Win 280 / Loss 350 / Flat 514) / skip 1500件
- 成長率目線: 平均log +0.000361 / 幾何平均 +0.036% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GUA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $151.21

## 4. Latest Market Context

- 更新: 2026-06-08T16:12:39.171903+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.11% price=63813.5
- Funnel: target 777 → liquid 150 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PIPPIN/USDT:USDT | +3.98% | $17,785,397.71 |
| BLESS/USDT:USDT | +3.53% | $10,038,476.62 |
| RAVE/USDT:USDT | +3.28% | $3,158,110.08 |
| FHE/USDT:USDT | +3.08% | $1,365,526.60 |
| SIREN/USDT:USDT | +2.68% | $25,729,321.11 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PIPPIN/USDT:USDT | below_1h_threshold | +3.99% | +3.88% |
| BLESS/USDT:USDT | below_1h_threshold | +3.54% | +3.43% |
| RAVE/USDT:USDT | below_1h_threshold | +3.28% | +3.18% |
| FHE/USDT:USDT | below_1h_threshold | +3.09% | +2.98% |
| SIREN/USDT:USDT | below_1h_threshold | +2.73% | +2.62% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
