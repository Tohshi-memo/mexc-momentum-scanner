# Decision Report

- generated_at: 2026-08-15T05:26:30.648898+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11636**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.75% / filled 20/20。**
- 全期間 MARKET基準: n=11636, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.75%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.75% | **+1.75%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.75% | **+1.75%** |
| LIMIT_1PCT | 16/20 | 80.0% | +1.44% | **+1.15%** |
| LIMIT_6PCT | 4/20 | 20.0% | +3.42% | **+0.68%** |
| LIMIT_5PCT | 6/20 | 30.0% | +2.13% | **+0.64%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 7/20 | 35.0% | +3.07% | **+1.07%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +6.07% | **+0.91%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.79% | **+0.36%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.50% | **+0.20%** |
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | -0.07% | **-0.05%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$636.46** / 初期 $100.00 (+536.46%)
- 確定: 4104件 (Win 1285 / Loss 1352 / Flat 1467) / skip 4093件
- 成長率目線: 平均log +0.000451 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ACE/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $636.46

## 4. Robust Adaptive DryRun ($100)

- 残高: **$153.76** / 初期 $100.00 (+53.76%)
- 確定: 1699件 (Win 486 / Loss 409 / Flat 804) / skip 3348件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0310 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ACE/USDT:USDT `LIMIT_5PCT` TP_HIT account +0.69% 残高後 $153.76

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.76** / 初期 $100.00 (+17.76%)
- 確定: 1581件 (Win 481 / Loss 604 / Flat 496) / pending 5件 / skip 1522件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000177 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ACE/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $117.76

## 6. Latest Market Context

- 更新: 2026-08-15T05:26:18.672255+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=63099.0
- Funnel: target 985 → liquid 163 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 70.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ROBO/USDT:USDT | +33.13% | $4,864,575.96 |
| ONE/USDT:USDT | +19.09% | $1,548,301.75 |
| US/USDT:USDT | +17.87% | $6,432,058.72 |
| AIO/USDT:USDT | +15.58% | $1,436,331.80 |
| CYS/USDT:USDT | +15.17% | $16,316,381.84 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DOLO/USDT:USDT | below_1h_threshold | +4.51% | +4.50% |
| BEAT/USDT:USDT | below_1h_threshold | +3.51% | +3.50% |
| NIL/USDT:USDT | below_1h_threshold | +2.99% | +2.98% |
| ON/USDT:USDT | below_1h_threshold | +2.85% | +2.84% |
| US/USDT:USDT | below_1h_threshold | +2.79% | +2.78% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
