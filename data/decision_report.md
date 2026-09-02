# Decision Report

- generated_at: 2026-09-02T08:01:21.180052+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13321**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13321, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.83%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.83% | **-0.83%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 5/20 | 25.0% | +6.39% | **+1.60%** |
| LIMIT_10PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_ATR | 8/20 | 40.0% | +2.96% | **+1.18%** |
| LIMIT_BB3S | 9/19 | 47.4% | +2.49% | **+1.18%** |
| LIMIT_9PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +2.46% | **+1.60%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +3.97% | **+1.59%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.94% | **+1.36%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +2.17% | **+1.08%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +2.81% | **+0.98%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 198件 (TP 74 / SL 119 / EXP 5)
- 最新: FONE/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$828.72** / 初期 $100.00 (+728.72%)
- 確定: 4947件 (Win 1503 / Loss 1626 / Flat 1818) / skip 4935件
- 成長率目線: 平均log +0.000427 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FONE/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $828.72

## 4. Robust Adaptive DryRun ($100)

- 残高: **$175.70** / 初期 $100.00 (+75.70%)
- 確定: 2300件 (Win 639 / Loss 550 / Flat 1111) / skip 4432件
- 成長率目線: 平均log +0.000245 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0320 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: FONE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $175.70

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.68** / 初期 $100.00 (+14.68%)
- 確定: 2090件 (Win 610 / Loss 818 / Flat 662) / pending 3件 / skip 2701件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000303 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: FONE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $114.68

## 6. Latest Market Context

- 更新: 2026-09-02T08:01:12.138668+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=77469.3
- Funnel: target 1041 → liquid 158 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FONE/USDT:USDT | +51.69% | $1,664,778.58 |
| MAGMA/USDT:USDT | +43.67% | $6,654,784.98 |
| CASHCAT/USDT:USDT | +34.07% | $1,583,577.43 |
| BONER/USDT:USDT | +33.60% | $2,568,587.88 |
| UAI/USDT:USDT | +22.11% | $23,601,534.66 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BONER/USDT:USDT | below_1h_threshold | +0.75% | +0.72% |
| UAI/USDT:USDT | below_1h_threshold | +0.71% | +0.67% |
| FONE/USDT:USDT | below_1h_threshold | +0.68% | +0.64% |
| FF/USDT:USDT | below_1h_threshold | +0.48% | +0.45% |
| VIRTUAL/USDT:USDT | below_1h_threshold | +0.39% | +0.35% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
