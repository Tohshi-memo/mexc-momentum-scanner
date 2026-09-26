# Decision Report

- generated_at: 2026-09-26T02:06:18.355254+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15560**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.40% / filled 20/20。**
- 全期間 MARKET基準: n=15560, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.40% | **+0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.58% | **+1.50%** |
| LIMIT_BB3S | 4/19 | 21.1% | +3.37% | **+0.71%** |
| LIMIT_8PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_ATR | 10/20 | 50.0% | +0.97% | **+0.49%** |
| MARKET | 20/20 | 100.0% | +0.40% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +3.10% | **+1.24%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +2.55% | **+0.76%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.80% | **+0.76%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +2.00% | **+0.60%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +1.20% | **+0.48%** |

## 2. $100 Live Portfolio

- 残高: **$120.79** / 初期 $100.00 (+20.79%)
- 確定トレード: 223件 (TP 82 / SL 135 / EXP 6)
- 最新: BATON/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.79
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,195.54** / 初期 $100.00 (+1095.54%)
- 確定: 5922件 (Win 1745 / Loss 1899 / Flat 2278) / skip 6199件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BATON/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,195.54

## 4. Robust Adaptive DryRun ($100)

- 残高: **$255.25** / 初期 $100.00 (+155.25%)
- 確定: 3492件 (Win 956 / Loss 795 / Flat 1741) / skip 5479件
- 成長率目線: 平均log +0.000268 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0180 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BATON/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $255.25

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.07** / 初期 $100.00 (+19.07%)
- 確定: 3183件 (Win 935 / Loss 1262 / Flat 986) / pending 3件 / skip 3844件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000222 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BR/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $119.07

## 6. Latest Market Context

- 更新: 2026-09-26T02:06:07.316411+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=84019.7
- Funnel: target 1067 → liquid 169 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BATON/USDT:USDT | +44.47% | $1,401,342.73 |
| PHA/USDT:USDT | +16.79% | $27,212,426.64 |
| BR/USDT:USDT | +15.31% | $9,559,182.51 |
| H/USDT:USDT | +13.98% | $1,046,516.55 |
| SEI/USDT:USDT | +13.18% | $40,716,871.51 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AERO/USDT:USDT | below_1h_threshold | +1.22% | +1.24% |
| AVAX/USDT:USDT | below_1h_threshold | +0.99% | +1.02% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +0.78% | +0.80% |
| BATON/USDT:USDT | below_1h_threshold | +0.70% | +0.73% |
| ONE/USDT:USDT | below_1h_threshold | +0.62% | +0.64% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
