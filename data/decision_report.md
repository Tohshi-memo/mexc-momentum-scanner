# Decision Report

- generated_at: 2026-08-15T15:21:26.491685+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11678**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=11678, expectancy=-0.01%
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
| LIMIT_6PCT | 4/20 | 20.0% | +1.94% | **+0.39%** |
| LIMIT_8PCT | 3/20 | 15.0% | +2.57% | **+0.39%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.85% | **+0.77%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.43% | **+0.28%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.50% | **+0.20%** |
| MARKET_LONG | 20/20 | 100.0% | +0.00% | **+0.00%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | -0.18% | **-0.04%** |

## 2. $100 Live Portfolio

- 残高: **$121.53** / 初期 $100.00 (+21.53%)
- 確定トレード: 183件 (TP 71 / SL 107 / EXP 5)
- 最新: MOVR/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.53
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$641.37** / 初期 $100.00 (+541.37%)
- 確定: 4146件 (Win 1290 / Loss 1355 / Flat 1501) / skip 4093件
- 成長率目線: 平均log +0.000448 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CYS/USDT:USDT `LIMIT_10PCT_LONG` EXPIRED account +0.00% 残高後 $641.37

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.25** / 初期 $100.00 (+55.25%)
- 確定: 1741件 (Win 492 / Loss 413 / Flat 836) / skip 3348件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0859 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CYS/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $155.25

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.34** / 初期 $100.00 (+19.34%)
- 確定: 1617件 (Win 493 / Loss 613 / Flat 511) / pending 6件 / skip 1530件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000421 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CYS/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $119.34

## 6. Latest Market Context

- 更新: 2026-08-15T15:21:16.607524+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=63039.5
- Funnel: target 985 → liquid 144 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| COW/USDT:USDT | +47.20% | $9,449,839.53 |
| HEMI/USDT:USDT | +35.69% | $1,345,450.65 |
| CYS/USDT:USDT | +32.81% | $27,252,073.23 |
| AIO/USDT:USDT | +26.64% | $1,933,139.11 |
| WAL/USDT:USDT | +26.17% | $1,853,197.94 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIO/USDT:USDT | below_1h_threshold | +2.48% | +2.44% |
| PRL/USDT:USDT | below_1h_threshold | +1.71% | +1.66% |
| FARTCOIN/USDT:USDT | below_1h_threshold | +0.62% | +0.58% |
| JTO/USDT:USDT | below_1h_threshold | +0.55% | +0.51% |
| KORU/USDT:USDT | below_1h_threshold | +0.46% | +0.42% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
