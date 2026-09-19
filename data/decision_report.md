# Decision Report

- generated_at: 2026-09-19T06:21:26.251114+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15001**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.49% / filled 20/20。**
- 全期間 MARKET基準: n=15001, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.49%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.49% | **+1.49%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.49% | **+1.49%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.56% | **+1.17%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +5.30% | **+1.06%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.82% | **+0.70%** |
| LIMIT_3PCT | 12/20 | 60.0% | +0.63% | **+0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.19% | **+0.48%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.00% | **+0.40%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +0.82% | **+0.37%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +0.28% | **+0.13%** |

## 2. $100 Live Portfolio

- 残高: **$120.56** / 初期 $100.00 (+20.56%)
- 確定トレード: 215件 (TP 79 / SL 131 / EXP 5)
- 最新: BULLA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.56
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,195.40** / 初期 $100.00 (+1095.40%)
- 確定: 5640件 (Win 1691 / Loss 1829 / Flat 2120) / skip 5922件
- 成長率目線: 平均log +0.000440 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AR/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,195.40

## 4. Robust Adaptive DryRun ($100)

- 残高: **$239.14** / 初期 $100.00 (+139.14%)
- 確定: 3178件 (Win 878 / Loss 760 / Flat 1540) / skip 5234件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ONE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $239.14

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.22** / 初期 $100.00 (+22.22%)
- 確定: 2973件 (Win 880 / Loss 1175 / Flat 918) / pending 1件 / skip 3497件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000209 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SYN/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $122.22

## 6. Latest Market Context

- 更新: 2026-09-19T06:21:13.481583+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=80955.0
- Funnel: target 1050 → liquid 167 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +121.17% | $49,734,204.94 |
| ONE/USDT:USDT | +34.04% | $24,984,864.92 |
| SYN/USDT:USDT | +27.32% | $7,459,888.45 |
| AR/USDT:USDT | +22.40% | $6,588,941.75 |
| SAGA/USDT:USDT | +22.03% | $4,508,478.38 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CATE/USDT:USDT | below_1h_threshold | +2.22% | +2.29% |
| LIT/USDT:USDT | below_1h_threshold | +1.27% | +1.34% |
| STRK/USDT:USDT | below_1h_threshold | +0.98% | +1.06% |
| UNI/USDT:USDT | below_1h_threshold | +0.97% | +1.04% |
| STG/USDT:USDT | below_1h_threshold | +0.94% | +1.01% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
