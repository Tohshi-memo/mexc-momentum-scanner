# Decision Report

- generated_at: 2026-07-28T04:36:16.090396+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9678**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9678, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.43%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.43% | **-0.43%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 7/20 | 35.0% | +2.76% | **+0.97%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.21% | **+0.49%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_BB3S | 6/20 | 30.0% | +1.20% | **+0.36%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +3.05% | **+1.07%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +0.98% | **+0.98%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.71% | **+0.94%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.48% | **+0.81%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +0.96% | **+0.58%** |

## 2. $100 Live Portfolio

- 残高: **$106.92** / 初期 $100.00 (+6.92%)
- 確定トレード: 148件 (TP 51 / SL 92 / EXP 5)
- 最新: BANK/USDT:USDT TP_HIT PnL +8.00% 残高後 $106.92
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$469.10** / 初期 $100.00 (+369.10%)
- 確定: 3448件 (Win 1090 / Loss 1119 / Flat 1239) / skip 2791件
- 成長率目線: 平均log +0.000448 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: COTI/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $469.10

## 4. Robust Adaptive DryRun ($100)

- 残高: **$137.24** / 初期 $100.00 (+37.24%)
- 確定: 1225件 (Win 338 / Loss 275 / Flat 612) / skip 1864件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0418 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: COTI/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $137.24

## 5. Causal Adaptive DryRun ($100)

- 残高: **$107.92** / 初期 $100.00 (+7.92%)
- 確定: 698件 (Win 225 / Loss 267 / Flat 206) / pending 0件 / skip 447件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000083 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: COTI/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $107.92

## 6. Latest Market Context

- 更新: 2026-07-28T04:36:09.192082+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.15% price=63212.6
- Funnel: target 902 → liquid 174 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| COTI/USDT:USDT | +55.30% | $12,038,599.21 |
| ON/USDT:USDT | +19.18% | $14,158,043.83 |
| RIF/USDT:USDT | +18.09% | $7,461,496.39 |
| SOONNETWORK/USDT:USDT | +15.79% | $1,471,126.42 |
| BULLA/USDT:USDT | +14.78% | $1,076,277.05 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BULLA/USDT:USDT | below_1h_threshold | +3.69% | +3.84% |
| SOONNETWORK/USDT:USDT | below_1h_threshold | +2.60% | +2.75% |
| O/USDT:USDT | below_1h_threshold | +2.05% | +2.21% |
| JIMOTHY/USDT:USDT | below_1h_threshold | +1.30% | +1.45% |
| LIT/USDT:USDT | below_1h_threshold | +1.06% | +1.21% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
