# Decision Report

- generated_at: 2026-11-27T03:16:33.595204+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19753**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19753, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.59%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.59% | **-1.59%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 4/20 | 20.0% | +4.36% | **+0.87%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.38% | **+0.25%** |
| LIMIT_9PCT | 5/20 | 25.0% | +0.80% | **+0.20%** |
| LIMIT_8PCT | 5/20 | 25.0% | +0.80% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/6 | 100.0% | +3.65% | **+3.65%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +2.49% | **+2.37%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +3.35% | **+1.68%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.15% | **+1.61%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +2.67% | **+1.20%** |

## 2. $100 Live Portfolio

- 残高: **$121.76** / 初期 $100.00 (+21.76%)
- 確定トレード: 292件 (TP 106 / SL 176 / EXP 10)
- 最新: SNXX/USDT:USDT EXPIRED PnL +2.62% 残高後 $121.76
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,938.41** / 初期 $100.00 (+1838.41%)
- 確定: 7644件 (Win 2199 / Loss 2460 / Flat 2985) / skip 8670件
- 成長率目線: 平均log +0.000388 / 幾何平均 +0.039% per trade / maxDD +9.04%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BULLA/USDT:USDT `LIMIT_6PCT` SL_HIT account -0.50% 残高後 $1,938.41

## 4. Robust Adaptive DryRun ($100)

- 残高: **$470.67** / 初期 $100.00 (+370.67%)
- 確定: 5273件 (Win 1408 / Loss 1131 / Flat 2734) / skip 7891件
- 成長率目線: 平均log +0.000294 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0185 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BLUR/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.69% 残高後 $470.67

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7915件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000276 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-27T03:16:13.805919+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.34% price=61500.0
- Funnel: target 1097 → liquid 120 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 66.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BULLA/USDT:USDT | +79.07% | $14,836,440.63 |
| BIGTIME/USDT:USDT | +19.70% | $2,957,296.03 |
| BLUR/USDT:USDT | +15.00% | $1,258,539.02 |
| ONE/USDT:USDT | +12.44% | $1,297,041.45 |
| NES/USDT:USDT | +12.30% | $1,018,628.16 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SNXX/USDT:USDT | below_relative_strength | +5.11% | +4.77% |
| SOXL/USDT:USDT | below_1h_threshold | +4.18% | +3.84% |
| MUU/USDT:USDT | below_1h_threshold | +3.27% | +2.94% |
| KORU/USDT:USDT | below_1h_threshold | +2.91% | +2.57% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +2.68% | +2.34% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
