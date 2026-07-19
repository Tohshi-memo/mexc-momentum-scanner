# Decision Report

- generated_at: 2026-07-19T03:11:12.901747+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8996**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8996, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +6.73% | **+0.67%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_8PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +4.56% | **+0.46%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.53% | **+2.27%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +3.04% | **+2.13%** |
| MARKET_LONG | 20/20 | 100.0% | +1.40% | **+1.40%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +2.17% | **+0.98%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +1.84% | **+0.92%** |

## 2. $100 Live Portfolio

- 残高: **$110.80** / 初期 $100.00 (+10.80%)
- 確定トレード: 117件 (TP 43 / SL 69 / EXP 5)
- 最新: SKYAI/USDT:USDT EXPIRED PnL +0.79% 残高後 $110.80
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$368.74** / 初期 $100.00 (+268.74%)
- 確定: 3059件 (Win 951 / Loss 976 / Flat 1132) / skip 2498件
- 成長率目線: 平均log +0.000427 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: US/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $368.74

## 4. Robust Adaptive DryRun ($100)

- 残高: **$122.47** / 初期 $100.00 (+22.47%)
- 確定: 957件 (Win 241 / Loss 195 / Flat 521) / skip 1450件
- 成長率目線: 平均log +0.000212 / 幾何平均 +0.021% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.2280 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: US/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $122.47

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.47** / 初期 $100.00 (-0.53%)
- 確定: 200件 (Win 64 / Loss 108 / Flat 28) / pending 2件 / skip 264件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000595 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $99.47

## 6. Latest Market Context

- 更新: 2026-07-19T03:11:06.191821+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.15% price=64698.2
- Funnel: target 885 → liquid 123 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +122.85% | $34,599,486.53 |
| BANK/USDT:USDT | +32.70% | $18,557,882.93 |
| B/USDT:USDT | +18.86% | $34,462,547.40 |
| TLM/USDT:USDT | +17.37% | $3,107,027.31 |
| TRADOOR/USDT:USDT | +13.85% | $6,123,926.65 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TRADOOR/USDT:USDT | below_1h_threshold | +2.03% | +2.18% |
| MYX/USDT:USDT | below_1h_threshold | +1.54% | +1.69% |
| RE/USDT:USDT | below_1h_threshold | +1.37% | +1.52% |
| ZBT/USDT:USDT | below_1h_threshold | +1.33% | +1.48% |
| ORDI/USDT:USDT | below_1h_threshold | +0.91% | +1.06% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
