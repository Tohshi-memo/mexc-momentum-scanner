# Decision Report

- generated_at: 2026-09-22T02:31:24.291373+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15288**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.43% / filled 20/20。**
- 全期間 MARKET基準: n=15288, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.43%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.43% | **+1.43%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.43% | **+1.43%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.30% | **+1.17%** |
| LIMIT_BB3S | 9/16 | 56.2% | +1.47% | **+0.83%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.07% | **+0.37%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +0.39% | **+0.39%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +0.37% | **+0.17%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +0.12% | **+0.10%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.18% | **+0.08%** |
| MARKET_LONG | 20/20 | 100.0% | +0.03% | **+0.03%** |

## 2. $100 Live Portfolio

- 残高: **$120.44** / 初期 $100.00 (+20.44%)
- 確定トレード: 216件 (TP 79 / SL 132 / EXP 5)
- 最新: PIEVERSE/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.44
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,177.18** / 初期 $100.00 (+1077.18%)
- 確定: 5779件 (Win 1719 / Loss 1859 / Flat 2201) / skip 6070件
- 成長率目線: 平均log +0.000427 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: KERNEL/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +1.00% 残高後 $1,177.18

## 4. Robust Adaptive DryRun ($100)

- 残高: **$248.74** / 初期 $100.00 (+148.74%)
- 確定: 3327件 (Win 919 / Loss 770 / Flat 1638) / skip 5372件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0310 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KERNEL/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.69% 残高後 $248.74

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.77** / 初期 $100.00 (+22.77%)
- 確定: 3060件 (Win 900 / Loss 1197 / Flat 963) / pending 3件 / skip 3695件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000244 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: KERNEL/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.34% 残高後 $122.77

## 6. Latest Market Context

- 更新: 2026-09-22T02:31:13.039358+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.12% price=85690.0
- Funnel: target 1055 → liquid 179 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 93.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| KERNEL/USDT:USDT | +47.48% | $2,160,500.89 |
| FORM/USDT:USDT | +24.76% | $9,042,536.43 |
| ALCH/USDT:USDT | +18.71% | $2,394,555.44 |
| GRASS/USDT:USDT | +13.78% | $2,352,873.69 |
| TAO/USDT:USDT | +11.64% | $141,257,455.94 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ONE/USDT:USDT | below_1h_threshold | +4.97% | +4.84% |
| GRASS/USDT:USDT | below_1h_threshold | +3.37% | +3.24% |
| RENDER/USDT:USDT | below_1h_threshold | +2.49% | +2.37% |
| SEI/USDT:USDT | below_1h_threshold | +2.22% | +2.10% |
| RAY/USDT:USDT | below_1h_threshold | +2.18% | +2.06% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
