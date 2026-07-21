# Decision Report

- generated_at: 2026-07-21T03:21:14.131358+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9146**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.94% / filled 20/20。**
- 全期間 MARKET基準: n=9146, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.94%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.94% | **+0.94%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +5.40% | **+1.08%** |
| MARKET | 20/20 | 100.0% | +0.94% | **+0.94%** |
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.98% | **+0.50%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.28% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.44% | **+1.30%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.14% | **+0.92%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +1.05% | **+0.79%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +3.22% | **+0.64%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |

## 2. $100 Live Portfolio

- 残高: **$108.59** / 初期 $100.00 (+8.59%)
- 確定トレード: 124件 (TP 44 / SL 75 / EXP 5)
- 最新: ZHIPUSTOCK/USDT:USDT SL_HIT PnL -3.93% 残高後 $108.59
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$419.26** / 初期 $100.00 (+319.26%)
- 確定: 3208件 (Win 1006 / Loss 1020 / Flat 1182) / skip 2499件
- 成長率目線: 平均log +0.000447 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ZHIPUSTOCK/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $419.26

## 4. Robust Adaptive DryRun ($100)

- 残高: **$130.91** / 初期 $100.00 (+30.91%)
- 確定: 1107件 (Win 292 / Loss 228 / Flat 587) / skip 1450件
- 成長率目線: 平均log +0.000243 / 幾何平均 +0.024% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1147 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ZHIPUSTOCK/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $130.91

## 5. Causal Adaptive DryRun ($100)

- 残高: **$101.26** / 初期 $100.00 (+1.26%)
- 確定: 339件 (Win 120 / Loss 150 / Flat 69) / pending 2件 / skip 279件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000277 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ZHIPUSTOCK/USDT:USDT `MARKET_LONG` EXPIRED account +0.17% 残高後 $101.26

## 6. Latest Market Context

- 更新: 2026-07-21T03:21:08.772441+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.12% price=65465.6
- Funnel: target 885 → liquid 172 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ERA/USDT:USDT | +70.18% | $2,285,821.69 |
| JIMOTHY/USDT:USDT | +21.98% | $2,845,743.91 |
| ZHIPUSTOCK/USDT:USDT | +21.40% | $1,386,827.88 |
| BLESS/USDT:USDT | +14.51% | $2,079,540.56 |
| ON/USDT:USDT | +12.79% | $2,061,183.99 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ERA/USDT:USDT | below_1h_threshold | +4.06% | +3.94% |
| ON/USDT:USDT | below_1h_threshold | +3.13% | +3.01% |
| KORU/USDT:USDT | below_1h_threshold | +2.97% | +2.85% |
| ESPORTS/USDT:USDT | below_1h_threshold | +2.30% | +2.18% |
| RE/USDT:USDT | below_1h_threshold | +2.13% | +2.00% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
