# Decision Report

- generated_at: 2026-08-26T14:16:20.294726+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12717**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12717, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.63%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.63% | **-0.63%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_7PCT | 7/20 | 35.0% | +2.11% | **+0.74%** |
| LIMIT_9PCT | 4/20 | 20.0% | +1.15% | **+0.23%** |
| LIMIT_8PCT | 5/20 | 25.0% | +0.80% | **+0.20%** |
| LIMIT_6PCT | 11/20 | 55.0% | +0.34% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.54% | **+1.16%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.76% | **+0.97%** |
| MARKET_LONG | 20/20 | 100.0% | +0.79% | **+0.79%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.10% | **+0.66%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +1.32% | **+0.66%** |

## 2. $100 Live Portfolio

- 残高: **$121.16** / 初期 $100.00 (+21.16%)
- 確定トレード: 192件 (TP 73 / SL 114 / EXP 5)
- 最新: CATE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.16
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$710.24** / 初期 $100.00 (+610.24%)
- 確定: 4616件 (Win 1403 / Loss 1516 / Flat 1697) / skip 4662件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ONT/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $710.24

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.51** / 初期 $100.00 (+56.51%)
- 確定: 2001件 (Win 544 / Loss 483 / Flat 974) / skip 4127件
- 成長率目線: 平均log +0.000224 / 幾何平均 +0.022% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0880 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BICO/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $156.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.00** / 初期 $100.00 (+16.00%)
- 確定: 1980件 (Win 580 / Loss 756 / Flat 644) / pending 2件 / skip 2209件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000331 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ONG/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $116.00

## 6. Latest Market Context

- 更新: 2026-08-26T14:16:11.426106+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=78430.7
- Funnel: target 1023 → liquid 165 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTR/USDT:USDT | +309.98% | $21,474,276.76 |
| TAC/USDT:USDT | +79.87% | $9,250,208.79 |
| ONG/USDT:USDT | +56.38% | $13,631,664.63 |
| BMT/USDT:USDT | +51.45% | $16,716,609.54 |
| LONGXIA/USDT:USDT | +36.79% | $2,031,104.71 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ONT/USDT:USDT | below_1h_threshold | +4.62% | +4.59% |
| MUU/USDT:USDT | below_1h_threshold | +3.51% | +3.48% |
| AMDSTOCK/USDT:USDT | below_1h_threshold | +3.43% | +3.40% |
| CASHCAT/USDT:USDT | below_1h_threshold | +3.31% | +3.28% |
| CRCLSTOCK/USDT:USDT | below_1h_threshold | +2.55% | +2.52% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
