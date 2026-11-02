# Decision Report

- generated_at: 2026-11-02T23:06:38.207833+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18042**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18042, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.06%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.06% | **+0.06%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 4/20 | 20.0% | +8.00% | **+1.60%** |
| LIMIT_7PCT | 5/20 | 25.0% | +5.92% | **+1.48%** |
| LIMIT_9PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_ATR | 15/20 | 75.0% | +1.56% | **+1.17%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.92% | **+0.67%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +2.77% | **+1.52%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +2.44% | **+1.22%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +2.26% | **+1.01%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +1.61% | **+0.97%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +1.29% | **+0.91%** |

## 2. $100 Live Portfolio

- 残高: **$121.74** / 初期 $100.00 (+21.74%)
- 確定トレード: 260件 (TP 96 / SL 156 / EXP 8)
- 最新: EVAA/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.74
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,556.02** / 初期 $100.00 (+1456.02%)
- 確定: 6894件 (Win 1999 / Loss 2211 / Flat 2684) / skip 7709件
- 成長率目線: 平均log +0.000398 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `MARKET` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EVAA/USDT:USDT `LIMIT_6PCT` SL_HIT account +0.24% 残高後 $1,556.02

## 4. Robust Adaptive DryRun ($100)

- 残高: **$381.70** / 初期 $100.00 (+281.70%)
- 確定: 4481件 (Win 1204 / Loss 1000 / Flat 2277) / skip 6972件
- 成長率目線: 平均log +0.000299 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score -0.0104 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: EVAA/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +0.69% 残高後 $381.70

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6203件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000174 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-02T23:06:20.281387+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.25% price=76725.6
- Funnel: target 1093 → liquid 162 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IDOL/USDT:USDT | +25.22% | $17,370,513.54 |
| EVAA/USDT:USDT | +16.37% | $6,197,740.72 |
| Q/USDT:USDT | +13.36% | $5,730,333.51 |
| SOXS/USDT:USDT | +10.66% | $23,855,353.67 |
| JCT/USDT:USDT | +7.82% | $2,118,350.85 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| Q/USDT:USDT | below_1h_threshold | +1.58% | +1.83% |
| SQQQ/USDT:USDT | below_1h_threshold | +0.49% | +0.73% |
| XMR/USDT:USDT | below_1h_threshold | +0.28% | +0.53% |
| BLESS/USDT:USDT | below_1h_threshold | +0.16% | +0.41% |
| ASTER/USDT:USDT | below_1h_threshold | +0.16% | +0.41% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
