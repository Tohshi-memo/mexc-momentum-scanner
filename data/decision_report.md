# Decision Report

- generated_at: 2026-10-17T01:26:15.785981+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16838**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=16838, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.55%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.55% | **-1.55%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 12/20 | 60.0% | +1.06% | **+0.64%** |
| LIMIT_7PCT | 6/20 | 30.0% | +2.00% | **+0.60%** |
| LIMIT_6PCT | 9/20 | 45.0% | +1.28% | **+0.58%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.52% | **+0.23%** |
| LIMIT_8PCT | 5/20 | 25.0% | +0.80% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +3.14% | **+1.88%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +3.39% | **+1.69%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +2.00% | **+1.20%** |
| LIMIT_BB3S_LONG | 6/7 | 85.7% | +1.28% | **+1.10%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +2.31% | **+1.04%** |

## 2. $100 Live Portfolio

- 残高: **$121.84** / 初期 $100.00 (+21.84%)
- 確定トレード: 243件 (TP 91 / SL 145 / EXP 7)
- 最新: CLAUDIA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.84
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,248.38** / 初期 $100.00 (+1148.38%)
- 確定: 6317件 (Win 1849 / Loss 2028 / Flat 2440) / skip 7082件
- 成長率目線: 平均log +0.000400 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AGT/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $1,248.38

## 4. Robust Adaptive DryRun ($100)

- 残高: **$274.05** / 初期 $100.00 (+174.05%)
- 確定: 3689件 (Win 1027 / Loss 878 / Flat 1784) / skip 6560件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.0824 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AGT/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $274.05

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5000件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000223 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-17T01:26:04.214151+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=81543.4
- Funnel: target 1084 → liquid 166 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AGT/USDT:USDT | +88.54% | $14,884,755.64 |
| ICNT/USDT:USDT | +20.00% | $3,085,571.91 |
| SIREN/USDT:USDT | +14.68% | $1,159,741.76 |
| UVXY/USDT:USDT | +12.38% | $2,825,967.88 |
| FOLKS/USDT:USDT | +10.39% | $1,250,315.75 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTW/USDT:USDT | below_1h_threshold | +3.12% | +3.10% |
| ICNT/USDT:USDT | below_1h_threshold | +2.53% | +2.52% |
| AKE/USDT:USDT | below_1h_threshold | +2.31% | +2.30% |
| SAND/USDT:USDT | below_1h_threshold | +1.12% | +1.11% |
| UVXY/USDT:USDT | below_1h_threshold | +1.07% | +1.06% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
