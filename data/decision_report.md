# Decision Report

- generated_at: 2026-09-04T07:46:31.499557+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13591**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.07% / filled 20/20。**
- 全期間 MARKET基準: n=13591, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.07%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.07% | **+1.07%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 18/20 | 90.0% | +1.64% | **+1.47%** |
| LIMIT_3PCT | 14/20 | 70.0% | +1.59% | **+1.12%** |
| LIMIT_ATR | 15/20 | 75.0% | +1.48% | **+1.11%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.14% | **+1.08%** |
| MARKET | 20/20 | 100.0% | +1.07% | **+1.07%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +4.89% | **+0.49%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.19% | **+0.48%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 199件 (TP 74 / SL 120 / EXP 5)
- 最新: MARSCOIN/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$859.66** / 初期 $100.00 (+759.66%)
- 確定: 5009件 (Win 1516 / Loss 1644 / Flat 1849) / skip 5143件
- 成長率目線: 平均log +0.000429 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BASECAT/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $859.66

## 4. Robust Adaptive DryRun ($100)

- 残高: **$185.77** / 初期 $100.00 (+85.77%)
- 確定: 2406件 (Win 680 / Loss 576 / Flat 1150) / skip 4596件
- 成長率目線: 平均log +0.000257 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0228 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TRIA/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $185.77

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.98** / 初期 $100.00 (+15.98%)
- 確定: 2244件 (Win 666 / Loss 878 / Flat 700) / pending 5件 / skip 2814件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000096 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: TRIA/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $115.98

## 6. Latest Market Context

- 更新: 2026-09-04T07:46:19.062390+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=80707.6
- Funnel: target 1051 → liquid 164 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TRIA/USDT:USDT | +39.07% | $5,240,547.76 |
| USELESS/USDT:USDT | +29.71% | $32,636,881.78 |
| HNT/USDT:USDT | +18.57% | $13,003,285.81 |
| PROM/USDT:USDT | +12.69% | $2,643,134.34 |
| ZEST/USDT:USDT | +10.55% | $1,139,341.63 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PONS/USDT:USDT | below_1h_threshold | +2.47% | +2.54% |
| AKE/USDT:USDT | below_1h_threshold | +1.08% | +1.15% |
| ZEC/USDT:USDT | below_1h_threshold | +1.00% | +1.07% |
| XMR/USDT:USDT | below_1h_threshold | +0.96% | +1.03% |
| ZRO/USDT:USDT | below_1h_threshold | +0.52% | +0.59% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
