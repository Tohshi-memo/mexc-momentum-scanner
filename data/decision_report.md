# Decision Report

- generated_at: 2026-09-25T00:51:26.531832+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15507**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.05% / filled 20/20。**
- 全期間 MARKET基準: n=15507, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.05%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.05% | **+1.05%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 5/20 | 25.0% | +4.92% | **+1.23%** |
| MARKET | 20/20 | 100.0% | +1.05% | **+1.05%** |
| LIMIT_8PCT | 6/20 | 30.0% | +3.28% | **+0.99%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.69% | **+0.63%** |
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 8/11 | 72.7% | +2.28% | **+1.66%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +0.77% | **+0.65%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.09% | **+0.31%** |
| MARKET_LONG | 20/20 | 100.0% | +0.30% | **+0.30%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +0.57% | **+0.29%** |

## 2. $100 Live Portfolio

- 残高: **$120.08** / 初期 $100.00 (+20.08%)
- 確定トレード: 219件 (TP 79 / SL 135 / EXP 5)
- 最新: XPL/USDT:USDT SL_HIT PnL -3.85% 残高後 $120.08
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,197.79** / 初期 $100.00 (+1097.79%)
- 確定: 5900件 (Win 1739 / Loss 1890 / Flat 2271) / skip 6168件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SAGA/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.00% 残高後 $1,197.79

## 4. Robust Adaptive DryRun ($100)

- 残高: **$252.66** / 初期 $100.00 (+152.66%)
- 確定: 3443件 (Win 949 / Loss 793 / Flat 1701) / skip 5475件
- 成長率目線: 平均log +0.000269 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SAGA/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.35% 残高後 $252.66

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.99** / 初期 $100.00 (+19.99%)
- 確定: 3170件 (Win 933 / Loss 1254 / Flat 983) / pending 1件 / skip 3806件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000086 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SAGA/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $119.99

## 6. Latest Market Context

- 更新: 2026-09-25T00:51:12.596093+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.28% price=84603.7
- Funnel: target 1069 → liquid 178 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SAGA/USDT:USDT | +30.90% | $11,845,720.14 |
| XPL/USDT:USDT | +11.51% | $15,210,931.99 |
| SYN/USDT:USDT | +10.92% | $2,066,746.66 |
| QNT/USDT:USDT | +9.90% | $3,578,753.28 |
| CHIP/USDT:USDT | +7.83% | $1,435,030.51 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| XPL/USDT:USDT | below_1h_threshold | +3.28% | +3.00% |
| ENA/USDT:USDT | below_1h_threshold | +3.19% | +2.91% |
| JTO/USDT:USDT | below_1h_threshold | +1.80% | +1.52% |
| XLM/USDT:USDT | below_1h_threshold | +1.77% | +1.49% |
| SUI/USDT:USDT | below_1h_threshold | +1.67% | +1.39% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
