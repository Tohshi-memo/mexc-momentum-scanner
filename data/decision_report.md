# Decision Report

- generated_at: 2026-10-03T19:21:21.254598+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16073**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=16073, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.12%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.12% | **-0.12%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.94% | **+0.42%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.17% | **+0.11%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.13% | **+0.04%** |
| LIMIT_1PCT | 19/20 | 95.0% | -0.02% | **-0.02%** |
| LIMIT_BB3S | 5/14 | 35.7% | -0.13% | **-0.04%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.38% | **+1.31%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.88% | **+0.62%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +1.03% | **+0.41%** |
| LIMIT_BB3S_LONG | 3/6 | 50.0% | +0.65% | **+0.32%** |
| LIMIT_6PCT_LONG | 5/20 | 25.0% | +1.17% | **+0.29%** |

## 2. $100 Live Portfolio

- 残高: **$120.27** / 初期 $100.00 (+20.27%)
- 確定トレード: 229件 (TP 82 / SL 140 / EXP 7)
- 最新: SI/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.27
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,291.26** / 初期 $100.00 (+1191.26%)
- 確定: 6146件 (Win 1812 / Loss 1972 / Flat 2362) / skip 6488件
- 成長率目線: 平均log +0.000416 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MANA/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account -0.46% 残高後 $1,291.26

## 4. Robust Adaptive DryRun ($100)

- 残高: **$274.46** / 初期 $100.00 (+174.46%)
- 確定: 3607件 (Win 1005 / Loss 845 / Flat 1757) / skip 5877件
- 成長率目線: 平均log +0.000280 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0191 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SI/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $274.46

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4234件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000184 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-03T19:21:11.952778+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=84807.2
- Funnel: target 1086 → liquid 137 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SPORTFUN/USDT:USDT | +17.56% | $1,240,507.18 |
| AIN/USDT:USDT | +11.12% | $2,934,536.42 |
| MOVR/USDT:USDT | +11.08% | $7,301,781.55 |
| PUMPFUN/USDT:USDT | +9.97% | $35,095,028.72 |
| VELVET/USDT:USDT | +6.96% | $16,841,975.34 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIN/USDT:USDT | below_1h_threshold | +3.41% | +3.52% |
| ONE/USDT:USDT | below_1h_threshold | +1.67% | +1.78% |
| SYN/USDT:USDT | below_1h_threshold | +1.53% | +1.64% |
| ZRO/USDT:USDT | below_1h_threshold | +1.10% | +1.21% |
| BTW/USDT:USDT | below_1h_threshold | +0.65% | +0.76% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
