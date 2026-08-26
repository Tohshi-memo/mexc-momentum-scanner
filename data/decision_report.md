# Decision Report

- generated_at: 2026-08-26T10:56:31.359748+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12697**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12697, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.50%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.50% | **-0.50%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 18/20 | 90.0% | +1.02% | **+0.92%** |
| LIMIT_BB3S | 8/17 | 47.1% | +1.28% | **+0.60%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.22% | **+0.49%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.29% | **+0.20%** |
| LIMIT_3PCT | 16/20 | 80.0% | -0.03% | **-0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.76% | **+1.68%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.86% | **+1.49%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +2.00% | **+1.20%** |
| LIMIT_5PCT_LONG | 7/20 | 35.0% | +1.62% | **+0.57%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +0.88% | **+0.44%** |

## 2. $100 Live Portfolio

- 残高: **$121.16** / 初期 $100.00 (+21.16%)
- 確定トレード: 192件 (TP 73 / SL 114 / EXP 5)
- 最新: CATE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.16
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$700.53** / 初期 $100.00 (+600.53%)
- 確定: 4598件 (Win 1399 / Loss 1511 / Flat 1688) / skip 4660件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PYTH/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $700.53

## 4. Robust Adaptive DryRun ($100)

- 残高: **$158.19** / 初期 $100.00 (+58.19%)
- 確定: 1993件 (Win 543 / Loss 478 / Flat 972) / skip 4115件
- 成長率目線: 平均log +0.000230 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1721 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PYTH/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $158.19

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.83** / 初期 $100.00 (+16.83%)
- 確定: 1970件 (Win 579 / Loss 750 / Flat 641) / pending 6件 / skip 2195件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000377 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BMT/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $116.83

## 6. Latest Market Context

- 更新: 2026-08-26T10:56:19.787962+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.38% price=78717.6
- Funnel: target 1023 → liquid 169 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 94.1 >= 65=1, 4h RSI 77.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTR/USDT:USDT | +213.02% | $14,608,843.87 |
| BMT/USDT:USDT | +59.13% | $14,949,430.14 |
| TAC/USDT:USDT | +54.27% | $6,826,743.75 |
| LONGXIA/USDT:USDT | +27.48% | $1,984,107.20 |
| PONS/USDT:USDT | +24.81% | $1,135,609.03 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BICO/USDT:USDT | below_1h_threshold | +3.31% | +2.93% |
| CHIP/USDT:USDT | below_1h_threshold | +2.67% | +2.29% |
| PROM/USDT:USDT | below_1h_threshold | +2.29% | +1.91% |
| BMT/USDT:USDT | below_1h_threshold | +2.27% | +1.89% |
| CYS/USDT:USDT | below_1h_threshold | +2.17% | +1.79% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
