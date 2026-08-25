# Decision Report

- generated_at: 2026-08-25T00:51:40.078265+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12559**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12559, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.83%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.83% | **-0.83%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 6/20 | 30.0% | +2.41% | **+0.72%** |
| LIMIT_8PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.40% | **+0.48%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.94% | **+0.39%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.48% | **+0.36%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +3.15% | **+2.05%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +2.33% | **+1.86%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +2.67% | **+1.73%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +2.34% | **+1.29%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +2.20% | **+0.99%** |

## 2. $100 Live Portfolio

- 残高: **$121.16** / 初期 $100.00 (+21.16%)
- 確定トレード: 192件 (TP 73 / SL 114 / EXP 5)
- 最新: CATE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.16
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$701.65** / 初期 $100.00 (+601.65%)
- 確定: 4539件 (Win 1384 / Loss 1488 / Flat 1667) / skip 4581件
- 成長率目線: 平均log +0.000429 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CATE/USDT:USDT `LIMIT_4PCT_LONG` TP_HIT account +1.00% 残高後 $701.65

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.16** / 初期 $100.00 (+56.16%)
- 確定: 1973件 (Win 536 / Loss 471 / Flat 966) / skip 3997件
- 成長率目線: 平均log +0.000226 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0718 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.35% 残高後 $156.16

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.37** / 初期 $100.00 (+15.37%)
- 確定: 1913件 (Win 561 / Loss 728 / Flat 624) / pending 0件 / skip 2121件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000192 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BTW/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $115.37

## 6. Latest Market Context

- 更新: 2026-08-25T00:51:24.165191+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.80% price=79587.0
- Funnel: target 1022 → liquid 185 → pre 50 → checked 50 → surge 4 → strict 1
- Surge前reject: below_1h_threshold=45, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.2 >= 65=1, 4h RSI 68.1 >= 65=1, 4h RSI 86.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +111.22% | $3,775,408.95 |
| TAC/USDT:USDT | +32.50% | $1,242,964.77 |
| CASHCAT/USDT:USDT | +25.66% | $2,546,786.03 |
| STORJ/USDT:USDT | +21.56% | $5,296,809.32 |
| ONG/USDT:USDT | +18.32% | $3,128,609.73 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| JUP/USDT:USDT | below_relative_strength | +5.12% | +4.32% |
| TAC/USDT:USDT | below_1h_threshold | +4.66% | +3.86% |
| PYTH/USDT:USDT | below_1h_threshold | +3.08% | +2.27% |
| DASH/USDT:USDT | below_1h_threshold | +2.86% | +2.06% |
| USELESS/USDT:USDT | below_1h_threshold | +2.85% | +2.05% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
