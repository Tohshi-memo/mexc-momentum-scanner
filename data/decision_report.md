# Decision Report

- generated_at: 2026-08-01T07:11:29.874257+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10069**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.34% / filled 20/20。**
- 全期間 MARKET基準: n=10069, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.34%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.34% | **+0.34%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +6.73% | **+0.67%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +4.39% | **+0.66%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| MARKET | 20/20 | 100.0% | +0.34% | **+0.34%** |
| LIMIT_ATR | 10/20 | 50.0% | +0.44% | **+0.22%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.83% | **+0.58%** |
| MARKET_LONG | 20/20 | 100.0% | +0.52% | **+0.52%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +0.80% | **+0.48%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.48% | **+0.41%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +1.33% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$567.22** / 初期 $100.00 (+467.22%)
- 確定: 3621件 (Win 1155 / Loss 1186 / Flat 1280) / skip 3009件
- 成長率目線: 平均log +0.000479 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GIGGLE/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account -0.20% 残高後 $567.22

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.81** / 初期 $100.00 (+40.81%)
- 確定: 1279件 (Win 359 / Loss 297 / Flat 623) / skip 2201件
- 成長率目線: 平均log +0.000268 / 幾何平均 +0.027% per trade / maxDD +3.89%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KOMA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $140.81

## 5. Causal Adaptive DryRun ($100)

- 残高: **$111.40** / 初期 $100.00 (+11.40%)
- 確定: 882件 (Win 284 / Loss 350 / Flat 248) / pending 6件 / skip 656件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000103 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: GIGGLE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $111.40

## 6. Latest Market Context

- 更新: 2026-08-01T07:11:19.977845+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=63075.7
- Funnel: target 921 → liquid 157 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +37.79% | $1,262,474.82 |
| GIGGLE/USDT:USDT | +28.44% | $28,895,387.79 |
| BTW/USDT:USDT | +27.13% | $4,116,600.22 |
| KOMA/USDT:USDT | +26.59% | $16,804,844.46 |
| TLM/USDT:USDT | +21.48% | $2,083,689.77 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| KOMA/USDT:USDT | below_1h_threshold | +2.68% | +2.64% |
| BEAT/USDT:USDT | below_1h_threshold | +1.54% | +1.50% |
| UB/USDT:USDT | below_1h_threshold | +1.18% | +1.14% |
| TLM/USDT:USDT | below_1h_threshold | +0.98% | +0.94% |
| ZAMA/USDT:USDT | below_1h_threshold | +0.83% | +0.79% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
