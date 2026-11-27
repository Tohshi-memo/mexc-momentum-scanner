# Decision Report

- generated_at: 2026-11-27T03:11:32.907496+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19751**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19751, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.59%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.59% | **-1.59%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 5/20 | 25.0% | +5.09% | **+1.27%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_9PCT | 6/20 | 30.0% | +2.00% | **+0.60%** |
| LIMIT_8PCT | 6/20 | 30.0% | +2.00% | **+0.60%** |
| LIMIT_ATR | 12/20 | 60.0% | -0.26% | **-0.15%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/5 | 100.0% | +4.92% | **+4.92%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +2.02% | **+1.92%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +4.17% | **+1.88%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.15% | **+1.61%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +3.20% | **+1.60%** |

## 2. $100 Live Portfolio

- 残高: **$121.76** / 初期 $100.00 (+21.76%)
- 確定トレード: 292件 (TP 106 / SL 176 / EXP 10)
- 最新: SNXX/USDT:USDT EXPIRED PnL +2.62% 残高後 $121.76
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,938.41** / 初期 $100.00 (+1838.41%)
- 確定: 7644件 (Win 2199 / Loss 2460 / Flat 2985) / skip 8668件
- 成長率目線: 平均log +0.000388 / 幾何平均 +0.039% per trade / maxDD +9.04%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BULLA/USDT:USDT `LIMIT_6PCT` SL_HIT account -0.50% 残高後 $1,938.41

## 4. Robust Adaptive DryRun ($100)

- 残高: **$467.46** / 初期 $100.00 (+367.46%)
- 確定: 5272件 (Win 1407 / Loss 1131 / Flat 2734) / skip 7890件
- 成長率目線: 平均log +0.000293 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BLUR/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.69% 残高後 $467.46

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7914件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000220 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-27T03:11:18.694144+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.47% price=61584.0
- Funnel: target 1097 → liquid 120 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 65.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BULLA/USDT:USDT | +77.27% | $14,787,931.72 |
| BIGTIME/USDT:USDT | +19.79% | $2,935,086.07 |
| BLUR/USDT:USDT | +14.33% | $1,210,526.03 |
| ONE/USDT:USDT | +13.49% | $1,290,833.51 |
| NES/USDT:USDT | +11.97% | $1,018,238.32 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SNXX/USDT:USDT | below_relative_strength | +5.11% | +4.63% |
| SOXL/USDT:USDT | below_1h_threshold | +4.18% | +3.71% |
| AIOT/USDT:USDT | below_1h_threshold | +3.28% | +2.80% |
| MUU/USDT:USDT | below_1h_threshold | +3.27% | +2.80% |
| KORU/USDT:USDT | below_1h_threshold | +2.91% | +2.44% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
