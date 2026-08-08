# Decision Report

- generated_at: 2026-08-08T16:31:32.878070+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10865**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10865, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.46%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.46% | **-1.46%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +4.33% | **+1.08%** |
| LIMIT_7PCT | 3/20 | 15.0% | +6.27% | **+0.94%** |
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.96% | **+0.69%** |
| LIMIT_ATR | 16/20 | 80.0% | +0.84% | **+0.67%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +4.00% | **+2.40%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +2.36% | **+1.89%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +1.83% | **+1.83%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +3.78% | **+1.51%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.88% | **+1.22%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$645.91** / 初期 $100.00 (+545.91%)
- 確定: 3866件 (Win 1218 / Loss 1257 / Flat 1391) / skip 3560件
- 成長率目線: 平均log +0.000483 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CATE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $645.91

## 4. Robust Adaptive DryRun ($100)

- 残高: **$142.00** / 初期 $100.00 (+42.00%)
- 確定: 1511件 (Win 424 / Loss 360 / Flat 727) / skip 2765件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0945 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CAT/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $142.00

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.56** / 初期 $100.00 (+18.56%)
- 確定: 1231件 (Win 388 / Loss 472 / Flat 371) / pending 6件 / skip 1101件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000259 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $118.56

## 6. Latest Market Context

- 更新: 2026-08-08T16:31:23.943566+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=65029.3
- Funnel: target 961 → liquid 157 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.0 >= 65=1, 4h RSI 94.3 >= 65=1, 4h RSI 74.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ACE/USDT:USDT | +9.54% | $13,365,274.96 |
| TUT/USDT:USDT | +5.43% | $13,825,204.22 |
| SKYAI/USDT:USDT | +5.16% | $68,748,345.12 |
| TST/USDT:USDT | +4.84% | $1,021,909.82 |
| BLESS/USDT:USDT | +2.92% | $95,769,549.38 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TST/USDT:USDT | below_1h_threshold | +4.84% | +4.87% |
| POWER/USDT:USDT | below_1h_threshold | +2.92% | +2.95% |
| BLESS/USDT:USDT | below_1h_threshold | +2.87% | +2.90% |
| US/USDT:USDT | below_1h_threshold | +2.61% | +2.64% |
| CAP/USDT:USDT | below_1h_threshold | +2.07% | +2.10% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
