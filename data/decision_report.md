# Decision Report

- generated_at: 2026-09-07T07:51:15.635069+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13872**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13872, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.88%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.88% | **-0.88%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 4/20 | 20.0% | +2.85% | **+0.57%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.88% | **+0.44%** |
| LIMIT_ATR | 11/20 | 55.0% | +0.66% | **+0.37%** |
| LIMIT_9PCT | 3/20 | 15.0% | +1.72% | **+0.26%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +2.11% | **+2.01%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.16% | **+1.62%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +2.01% | **+1.30%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +2.30% | **+1.15%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.78% | **+0.98%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$849.14** / 初期 $100.00 (+749.14%)
- 確定: 5145件 (Win 1541 / Loss 1681 / Flat 1923) / skip 5288件
- 成長率目線: 平均log +0.000416 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_8PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MEMEROBINHOOD/USDT:USDT `LIMIT_8PCT` EXPIRED account +0.00% 残高後 $849.14

## 4. Robust Adaptive DryRun ($100)

- 残高: **$188.18** / 初期 $100.00 (+88.18%)
- 確定: 2571件 (Win 717 / Loss 618 / Flat 1236) / skip 4712件
- 成長率目線: 平均log +0.000246 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.0816 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $188.18

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.61** / 初期 $100.00 (+19.61%)
- 確定: 2464件 (Win 731 / Loss 936 / Flat 797) / pending 3件 / skip 2875件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_8PCT` (selected_by_causal_log_growth) / causal_score +0.000323 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MEMEROBINHOOD/USDT:USDT `LIMIT_8PCT` EXPIRED account +0.00% 残高後 $119.61

## 6. Latest Market Context

- 更新: 2026-09-07T07:51:06.177238+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.43% price=79276.9
- Funnel: target 1059 → liquid 142 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 66.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MEMEROBINHOOD/USDT:USDT | +301.99% | $1,688,879.63 |
| BONER/USDT:USDT | +123.12% | $5,212,600.23 |
| XAN/USDT:USDT | +12.29% | $2,337,503.14 |
| ICP/USDT:USDT | +11.99% | $10,303,106.49 |
| WLD/USDT:USDT | +11.48% | $53,466,374.86 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| WLD/USDT:USDT | below_1h_threshold | +4.07% | +4.50% |
| MAGMA/USDT:USDT | below_1h_threshold | +2.83% | +3.26% |
| ICP/USDT:USDT | below_1h_threshold | +2.01% | +2.44% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +0.79% | +1.21% |
| SAMSUNGSTOCK/USDT:USDT | below_1h_threshold | +0.77% | +1.19% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
