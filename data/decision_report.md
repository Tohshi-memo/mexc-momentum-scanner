# Decision Report

- generated_at: 2026-11-04T01:01:41.442979+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18098**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.26% / filled 20/20。**
- 全期間 MARKET基準: n=18098, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.26%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.26% | **+0.26%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 20/20 | 100.0% | +0.61% | **+0.61%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.79% | **+0.59%** |
| LIMIT_10PCT | 3/20 | 15.0% | +3.15% | **+0.47%** |
| LIMIT_BB3S | 9/17 | 52.9% | +0.85% | **+0.45%** |
| LIMIT_9PCT | 3/20 | 15.0% | +2.86% | **+0.43%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +1.77% | **+1.77%** |
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +1.47% | **+1.47%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +3.27% | **+0.65%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.87% | **+0.65%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +2.00% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$121.61** / 初期 $100.00 (+21.61%)
- 確定トレード: 261件 (TP 96 / SL 157 / EXP 8)
- 最新: IDOL/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.61
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,500.44** / 初期 $100.00 (+1400.44%)
- 確定: 6921件 (Win 2001 / Loss 2219 / Flat 2701) / skip 7738件
- 成長率目線: 平均log +0.000391 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ICNT/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $1,500.44

## 4. Robust Adaptive DryRun ($100)

- 残高: **$380.03** / 初期 $100.00 (+280.03%)
- 確定: 4512件 (Win 1208 / Loss 1004 / Flat 2300) / skip 6997件
- 成長率目線: 平均log +0.000296 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0660 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LYN/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $380.03

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6259件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000159 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-04T01:01:28.317816+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=77212.1
- Funnel: target 1084 → liquid 162 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CLANKER/USDT:USDT | +32.84% | $1,125,823.02 |
| BEAT/USDT:USDT | +6.37% | $11,400,751.23 |
| SMCISTOCK/USDT:USDT | +6.09% | $1,495,591.59 |
| SOXS/USDT:USDT | +5.59% | $27,679,071.10 |
| IDOL/USDT:USDT | +5.31% | $10,271,406.83 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOXS/USDT:USDT | below_1h_threshold | +3.91% | +3.92% |
| SQQQ/USDT:USDT | below_1h_threshold | +1.80% | +1.82% |
| LYN/USDT:USDT | below_1h_threshold | +0.89% | +0.90% |
| ALUMINUM/USDT:USDT | below_1h_threshold | +0.50% | +0.52% |
| Q/USDT:USDT | below_1h_threshold | +0.49% | +0.51% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
