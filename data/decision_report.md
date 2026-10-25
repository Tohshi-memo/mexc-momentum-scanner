# Decision Report

- generated_at: 2026-10-25T16:51:23.846157+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17433**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=17433, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.83% | **+0.73%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.69% | **+0.66%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_ATR | 5/20 | 25.0% | +1.01% | **+0.25%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +3.87% | **+1.55%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.40% | **+1.33%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +3.00% | **+1.20%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.30% | **+1.04%** |
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 250件 (TP 92 / SL 150 / EXP 8)
- 最新: MSTRSTOCK/USDT:USDT EXPIRED PnL +0.27% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,567.28** / 初期 $100.00 (+1467.28%)
- 確定: 6686件 (Win 1946 / Loss 2131 / Flat 2609) / skip 7308件
- 成長率目線: 平均log +0.000412 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: Q/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,567.28

## 4. Robust Adaptive DryRun ($100)

- 残高: **$318.18** / 初期 $100.00 (+218.18%)
- 確定: 3976件 (Win 1104 / Loss 935 / Flat 1937) / skip 6868件
- 成長率目線: 平均log +0.000291 / 幾何平均 +0.029% per trade / maxDD +4.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1925 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: Q/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $318.18

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5592件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000538 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-25T16:51:09.203000+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.00% price=80601.2
- Funnel: target 1070 → liquid 117 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BIRB/USDT:USDT | +2.10% | $1,827,725.47 |
| ORDER/USDT:USDT | +2.06% | $4,184,036.08 |
| VVV/USDT:USDT | +1.24% | $1,631,451.70 |
| NEAR/USDT:USDT | +1.12% | $122,228,467.78 |
| APR/USDT:USDT | +0.87% | $11,651,548.80 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BIRB/USDT:USDT | below_1h_threshold | +2.11% | +2.11% |
| ORDER/USDT:USDT | below_1h_threshold | +2.06% | +2.06% |
| VVV/USDT:USDT | below_1h_threshold | +1.27% | +1.27% |
| APR/USDT:USDT | below_1h_threshold | +1.09% | +1.09% |
| NEAR/USDT:USDT | below_1h_threshold | +1.06% | +1.06% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
