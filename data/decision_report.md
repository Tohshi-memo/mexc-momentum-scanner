# Decision Report

- generated_at: 2026-09-02T19:01:26.494268+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13372**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13372, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-3.41%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -3.41% | **-3.41%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_10PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_9PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +2.21% | **+0.77%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +3.41% | **+0.51%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +7.73% | **+7.73%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +4.07% | **+2.44%** |
| MARKET_LONG | 20/20 | 100.0% | +2.21% | **+2.21%** |
| LIMIT_4PCT_LONG | 6/20 | 30.0% | +6.02% | **+1.81%** |
| LIMIT_5PCT_LONG | 6/20 | 30.0% | +6.02% | **+1.81%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 198件 (TP 74 / SL 119 / EXP 5)
- 最新: FONE/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$882.23** / 初期 $100.00 (+782.23%)
- 確定: 4987件 (Win 1513 / Loss 1633 / Flat 1841) / skip 4946件
- 成長率目線: 平均log +0.000437 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.87% 残高後 $882.23

## 4. Robust Adaptive DryRun ($100)

- 残高: **$186.37** / 初期 $100.00 (+86.37%)
- 確定: 2351件 (Win 664 / Loss 564 / Flat 1123) / skip 4432件
- 成長率目線: 平均log +0.000265 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1806 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BONER/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $186.37

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.78** / 初期 $100.00 (+14.78%)
- 確定: 2093件 (Win 611 / Loss 819 / Flat 663) / pending 0件 / skip 2754件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000576 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CASHCAT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $114.78

## 6. Latest Market Context

- 更新: 2026-09-02T19:01:15.164841+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=77315.0
- Funnel: target 1044 → liquid 156 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +70.45% | $28,419,371.30 |
| BONER/USDT:USDT | +21.89% | $2,934,638.65 |
| FONE/USDT:USDT | +13.33% | $1,999,319.24 |
| MARSCOIN/USDT:USDT | +13.03% | $3,051,237.26 |
| BULLA/USDT:USDT | +12.25% | $2,003,053.26 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DELLSTOCK/USDT:USDT | below_1h_threshold | +4.39% | +4.43% |
| MUU/USDT:USDT | below_1h_threshold | +1.70% | +1.74% |
| BTW/USDT:USDT | below_1h_threshold | +1.70% | +1.73% |
| SKHYSTOCK/USDT:USDT | below_1h_threshold | +0.88% | +0.92% |
| MUSTOCK/USDT:USDT | below_1h_threshold | +0.86% | +0.90% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
