# Decision Report

- generated_at: 2026-05-28T03:29:38.511670+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4951**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.44% / filled 20/20。**
- 全期間 MARKET基準: n=4951, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=+0.44%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.44% | **+0.44%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 14/20 | 70.0% | +3.67% | **+2.57%** |
| LIMIT_2PCT | 16/20 | 80.0% | +2.56% | **+2.05%** |
| LIMIT_4PCT | 10/20 | 50.0% | +2.87% | **+1.44%** |
| LIMIT_1PCT | 16/20 | 80.0% | +1.18% | **+0.95%** |
| LIMIT_5PCT | 4/20 | 20.0% | +3.25% | **+0.65%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +3.62% | **+1.81%** |
| LIMIT_10PCT_LONG | 6/20 | 30.0% | +5.15% | **+1.55%** |
| LIMIT_9PCT_LONG | 7/20 | 35.0% | +3.36% | **+1.18%** |
| LIMIT_7PCT_LONG | 11/20 | 55.0% | +1.69% | **+0.93%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +0.86% | **+0.64%** |

## 2. $100 Live Portfolio

- 残高: **$97.15** / 初期 $100.00 (-2.85%)
- 確定トレード: 68件 (TP 19 / SL 46 / EXP 3)
- 最新: B/USDT:USDT TP_HIT PnL +6.46% 残高後 $97.15
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$126.79** / 初期 $100.00 (+26.79%)
- 確定: 687件 (Win 172 / Loss 220 / Flat 295) / skip 825件
- 成長率目線: 平均log +0.000346 / 幾何平均 +0.035% per trade / maxDD +4.72%
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_10PCT_LONG` EXPIRED account +0.00% 残高後 $126.79

## 4. Latest Market Context

- 更新: 2026-05-28T03:29:36.357300+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.69% price=73744.9
- Funnel: target 777 → liquid 152 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SNOWSTOCK/USDT:USDT | +34.67% | $7,158,370.18 |
| GENIUS/USDT:USDT | +13.37% | $2,056,976.36 |
| NBISSTOCK/USDT:USDT | +13.30% | $1,547,759.48 |
| BUILDONBOB/USDT:USDT | +7.02% | $1,023,707.95 |
| XLM/USDT:USDT | +6.98% | $84,346,812.46 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BUILDONBOB/USDT:USDT | below_1h_threshold | +2.03% | +2.72% |
| BEAT/USDT:USDT | below_1h_threshold | +2.02% | +2.71% |
| USOIL/USDT:USDT | below_1h_threshold | +0.55% | +1.24% |
| UKOIL/USDT:USDT | below_1h_threshold | +0.51% | +1.19% |
| RIF/USDT:USDT | below_1h_threshold | +0.12% | +0.80% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
