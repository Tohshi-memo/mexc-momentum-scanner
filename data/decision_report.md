# Decision Report

- generated_at: 2026-08-26T13:56:41.539652+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12715**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12715, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.12%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.12% | **-0.12%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_7PCT | 7/20 | 35.0% | +2.11% | **+0.74%** |
| LIMIT_9PCT | 4/20 | 20.0% | +1.15% | **+0.23%** |
| LIMIT_8PCT | 5/20 | 25.0% | +0.80% | **+0.20%** |
| LIMIT_BB3S | 8/15 | 53.3% | +0.24% | **+0.13%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.80% | **+1.44%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.39% | **+0.84%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.76% | **+0.49%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +0.89% | **+0.49%** |

## 2. $100 Live Portfolio

- 残高: **$121.16** / 初期 $100.00 (+21.16%)
- 確定トレード: 192件 (TP 73 / SL 114 / EXP 5)
- 最新: CATE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.16
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$703.90** / 初期 $100.00 (+603.90%)
- 確定: 4614件 (Win 1402 / Loss 1516 / Flat 1696) / skip 4662件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTR/USDT:USDT `LIMIT_3PCT_LONG` TP_HIT account +1.00% 残高後 $703.90

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.51** / 初期 $100.00 (+56.51%)
- 確定: 2001件 (Win 544 / Loss 483 / Flat 974) / skip 4125件
- 成長率目線: 平均log +0.000224 / 幾何平均 +0.022% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1012 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BICO/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $156.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.00** / 初期 $100.00 (+16.00%)
- 確定: 1980件 (Win 580 / Loss 756 / Flat 644) / pending 2件 / skip 2208件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000273 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ONG/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $116.00

## 6. Latest Market Context

- 更新: 2026-08-26T13:56:24.013473+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=78265.0
- Funnel: target 1023 → liquid 169 → pre 50 → checked 50 → surge 6 → strict 1
- Surge前reject: below_1h_threshold=44, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.6 >= 65=1, 4h RSI 83.8 >= 65=1, 4h RSI 96.0 >= 65=1, 4h RSI 67.6 >= 65=1, 4h RSI 66.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTR/USDT:USDT | +312.99% | $21,066,118.52 |
| TAC/USDT:USDT | +74.40% | $9,089,108.87 |
| BMT/USDT:USDT | +50.58% | $16,629,279.26 |
| LONGXIA/USDT:USDT | +44.67% | $2,022,355.11 |
| ONG/USDT:USDT | +42.47% | $12,021,639.78 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BR/USDT:USDT | below_1h_threshold | +2.93% | +2.95% |
| METASTOCK/USDT:USDT | below_1h_threshold | +2.27% | +2.29% |
| CAP/USDT:USDT | below_1h_threshold | +1.98% | +2.00% |
| STX/USDT:USDT | below_1h_threshold | +1.46% | +1.48% |
| BMT/USDT:USDT | below_1h_threshold | +1.04% | +1.06% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
