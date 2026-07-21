# Decision Report

- generated_at: 2026-07-21T12:51:27.761051+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9175**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9175, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.69%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.69% | **-1.69%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.95% | **+0.43%** |
| LIMIT_4PCT | 15/20 | 75.0% | +0.53% | **+0.40%** |
| LIMIT_BB3S | 10/17 | 58.8% | +0.58% | **+0.34%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +0.92% | **+0.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +2.83% | **+1.27%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.50% | **+1.05%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.13% | **+1.02%** |
| LIMIT_7PCT_LONG | 5/20 | 25.0% | +3.78% | **+0.95%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +5.62% | **+0.84%** |

## 2. $100 Live Portfolio

- 残高: **$107.51** / 初期 $100.00 (+7.51%)
- 確定トレード: 126件 (TP 44 / SL 77 / EXP 5)
- 最新: US/USDT:USDT SL_HIT PnL -4.00% 残高後 $107.51
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$424.55** / 初期 $100.00 (+324.55%)
- 確定: 3237件 (Win 1018 / Loss 1033 / Flat 1186) / skip 2499件
- 成長率目線: 平均log +0.000447 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ERA/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $424.55

## 4. Robust Adaptive DryRun ($100)

- 残高: **$132.43** / 初期 $100.00 (+32.43%)
- 確定: 1136件 (Win 305 / Loss 241 / Flat 590) / skip 1450件
- 成長率目線: 平均log +0.000247 / 幾何平均 +0.025% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0899 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ERA/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $132.43

## 5. Causal Adaptive DryRun ($100)

- 残高: **$100.91** / 初期 $100.00 (+0.91%)
- 確定: 341件 (Win 120 / Loss 152 / Flat 69) / pending 0件 / skip 309件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000227 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: 1000BONK/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $100.91

## 6. Latest Market Context

- 更新: 2026-07-21T12:51:19.018283+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.27% price=66495.2
- Funnel: target 885 → liquid 177 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.2 >= 65=1, 4h RSI 81.8 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PONS/USDT:USDT | +105.10% | $1,012,738.76 |
| JIMOTHY/USDT:USDT | +104.43% | $4,860,015.86 |
| ERA/USDT:USDT | +73.12% | $10,368,991.33 |
| ESPORTS/USDT:USDT | +34.90% | $7,138,268.56 |
| ZHIPUSTOCK/USDT:USDT | +32.45% | $3,192,615.91 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BULLA/USDT:USDT | below_1h_threshold | +3.42% | +3.15% |
| US/USDT:USDT | below_1h_threshold | +2.34% | +2.07% |
| LA/USDT:USDT | below_1h_threshold | +1.58% | +1.31% |
| LUNC/USDT:USDT | below_1h_threshold | +1.25% | +0.98% |
| BLESS/USDT:USDT | below_1h_threshold | +0.93% | +0.66% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
