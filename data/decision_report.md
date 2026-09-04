# Decision Report

- generated_at: 2026-09-04T06:26:30.200821+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13589**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.27% / filled 20/20。**
- 全期間 MARKET基準: n=13589, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+2.27%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.27% | **+2.27%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.27% | **+2.27%** |
| LIMIT_1PCT | 19/20 | 95.0% | +2.29% | **+2.18%** |
| LIMIT_2PCT | 17/20 | 85.0% | +2.44% | **+2.07%** |
| LIMIT_3PCT | 13/20 | 65.0% | +2.48% | **+1.61%** |
| LIMIT_ATR | 13/20 | 65.0% | +2.02% | **+1.31%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +4.89% | **+0.49%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.89% | **+0.40%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +0.74% | **+0.37%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 199件 (TP 74 / SL 120 / EXP 5)
- 最新: MARSCOIN/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$859.66** / 初期 $100.00 (+759.66%)
- 確定: 5009件 (Win 1516 / Loss 1644 / Flat 1849) / skip 5141件
- 成長率目線: 平均log +0.000429 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BASECAT/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $859.66

## 4. Robust Adaptive DryRun ($100)

- 残高: **$185.77** / 初期 $100.00 (+85.77%)
- 確定: 2404件 (Win 680 / Loss 576 / Flat 1148) / skip 4596件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0218 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $185.77

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.98** / 初期 $100.00 (+15.98%)
- 確定: 2242件 (Win 666 / Loss 878 / Flat 698) / pending 3件 / skip 2814件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000100 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $115.98

## 6. Latest Market Context

- 更新: 2026-09-04T06:26:22.435686+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.19% price=80800.6
- Funnel: target 1051 → liquid 161 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 70.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TRIA/USDT:USDT | +38.28% | $3,554,221.10 |
| HNT/USDT:USDT | +24.25% | $12,386,882.85 |
| USELESS/USDT:USDT | +21.34% | $30,979,697.68 |
| PROM/USDT:USDT | +14.50% | $2,505,858.50 |
| PONS/USDT:USDT | +11.93% | $9,761,615.12 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FF/USDT:USDT | below_1h_threshold | +1.46% | +1.64% |
| DASH/USDT:USDT | below_1h_threshold | +1.17% | +1.36% |
| MUBARAK/USDT:USDT | below_1h_threshold | +1.12% | +1.31% |
| KORU/USDT:USDT | below_1h_threshold | +0.91% | +1.10% |
| SOXL/USDT:USDT | below_1h_threshold | +0.90% | +1.08% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
