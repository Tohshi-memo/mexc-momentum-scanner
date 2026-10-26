# Decision Report

- generated_at: 2026-10-26T22:56:16.901519+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17530**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17530, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.06%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.06% | **-1.06%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 7/12 | 58.3% | +4.57% | **+2.67%** |
| LIMIT_8PCT | 8/20 | 40.0% | +5.00% | **+2.00%** |
| LIMIT_7PCT | 9/20 | 45.0% | +3.42% | **+1.54%** |
| LIMIT_6PCT | 12/20 | 60.0% | +2.45% | **+1.47%** |
| LIMIT_ATR | 16/20 | 80.0% | +1.77% | **+1.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +2.92% | **+2.62%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +3.03% | **+2.28%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +2.18% | **+2.07%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +2.19% | **+1.09%** |
| LIMIT_BB3S_LONG | 5/8 | 62.5% | +0.76% | **+0.48%** |

## 2. $100 Live Portfolio

- 残高: **$121.62** / 初期 $100.00 (+21.62%)
- 確定トレード: 252件 (TP 93 / SL 151 / EXP 8)
- 最新: Q/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.62
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,526.92** / 初期 $100.00 (+1426.92%)
- 確定: 6721件 (Win 1956 / Loss 2152 / Flat 2613) / skip 7370件
- 成長率目線: 平均log +0.000406 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: Q/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $1,526.92

## 4. Robust Adaptive DryRun ($100)

- 残高: **$324.96** / 初期 $100.00 (+224.96%)
- 確定: 4059件 (Win 1120 / Loss 953 / Flat 1986) / skip 6882件
- 成長率目線: 平均log +0.000290 / 幾何平均 +0.029% per trade / maxDD +4.13%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0821 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PONS/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $324.96

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5693件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000361 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-26T22:56:07.001174+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.15% price=79953.3
- Funnel: target 1078 → liquid 159 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| Q/USDT:USDT | +234.42% | $19,823,520.33 |
| DNA/USDT:USDT | +5.40% | $1,216,606.75 |
| AGT/USDT:USDT | +5.31% | $1,753,409.90 |
| DODO/USDT:USDT | +5.26% | $1,361,065.77 |
| BAT/USDT:USDT | +3.77% | $2,251,741.43 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| IRYS/USDT:USDT | below_1h_threshold | +4.15% | +4.29% |
| BAT/USDT:USDT | below_1h_threshold | +1.94% | +2.09% |
| ORDER/USDT:USDT | below_1h_threshold | +1.85% | +1.99% |
| DODO/USDT:USDT | below_1h_threshold | +1.83% | +1.98% |
| DNA/USDT:USDT | below_1h_threshold | +1.31% | +1.46% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
