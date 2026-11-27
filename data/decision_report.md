# Decision Report

- generated_at: 2026-11-27T03:41:19.239808+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19755**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19755, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.39%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.39% | **-0.39%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_10PCT | 3/20 | 15.0% | +3.15% | **+0.47%** |
| LIMIT_7PCT | 5/20 | 25.0% | +0.80% | **+0.20%** |
| LIMIT_6PCT | 7/20 | 35.0% | +0.24% | **+0.08%** |
| LIMIT_2PCT | 18/20 | 90.0% | +0.02% | **+0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 7/7 | 100.0% | +2.55% | **+2.55%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +2.49% | **+2.37%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.15% | **+1.61%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +2.13% | **+1.28%** |
| MARKET_LONG | 20/20 | 100.0% | +0.79% | **+0.79%** |

## 2. $100 Live Portfolio

- 残高: **$121.76** / 初期 $100.00 (+21.76%)
- 確定トレード: 292件 (TP 106 / SL 176 / EXP 10)
- 最新: SNXX/USDT:USDT EXPIRED PnL +2.62% 残高後 $121.76
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,938.41** / 初期 $100.00 (+1838.41%)
- 確定: 7644件 (Win 2199 / Loss 2460 / Flat 2985) / skip 8672件
- 成長率目線: 平均log +0.000388 / 幾何平均 +0.039% per trade / maxDD +9.04%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BULLA/USDT:USDT `LIMIT_6PCT` SL_HIT account -0.50% 残高後 $1,938.41

## 4. Robust Adaptive DryRun ($100)

- 残高: **$467.38** / 初期 $100.00 (+367.38%)
- 確定: 5275件 (Win 1408 / Loss 1133 / Flat 2734) / skip 7891件
- 成長率目線: 平均log +0.000292 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0185 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BULLA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $467.38

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7916件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000197 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-27T03:41:06.855906+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.40% price=61536.1
- Funnel: target 1097 → liquid 122 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 67.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BULLA/USDT:USDT | +72.94% | $15,083,540.16 |
| BIGTIME/USDT:USDT | +23.12% | $3,030,689.10 |
| ONE/USDT:USDT | +12.14% | $1,342,544.25 |
| BLUR/USDT:USDT | +11.93% | $1,467,523.50 |
| SNXX/USDT:USDT | +11.80% | $3,896,583.92 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SNXX/USDT:USDT | below_relative_strength | +5.11% | +4.71% |
| SOXL/USDT:USDT | below_1h_threshold | +4.18% | +3.78% |
| MUU/USDT:USDT | below_1h_threshold | +3.27% | +2.88% |
| MANTRA/USDT:USDT | below_1h_threshold | +3.20% | +2.81% |
| KORU/USDT:USDT | below_1h_threshold | +2.91% | +2.52% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
