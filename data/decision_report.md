# Decision Report

- generated_at: 2026-09-01T22:46:30.053143+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13276**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13276, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.11%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.11% | **-1.11%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 6/20 | 30.0% | +5.85% | **+1.76%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +3.12% | **+1.40%** |
| LIMIT_7PCT | 6/20 | 30.0% | +4.54% | **+1.36%** |
| LIMIT_6PCT | 7/20 | 35.0% | +3.63% | **+1.27%** |
| LIMIT_9PCT | 3/20 | 15.0% | +6.86% | **+1.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +3.53% | **+1.76%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +2.39% | **+1.55%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.67% | **+1.50%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +3.65% | **+1.46%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.42% | **+1.13%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 196件 (TP 73 / SL 118 / EXP 5)
- 最新: BTR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$820.27** / 初期 $100.00 (+720.27%)
- 確定: 4911件 (Win 1496 / Loss 1615 / Flat 1800) / skip 4926件
- 成長率目線: 平均log +0.000429 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FONE/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $820.27

## 4. Robust Adaptive DryRun ($100)

- 残高: **$175.33** / 初期 $100.00 (+75.33%)
- 確定: 2255件 (Win 631 / Loss 541 / Flat 1083) / skip 4432件
- 成長率目線: 平均log +0.000249 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.1044 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: FONE/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $175.33

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.88** / 初期 $100.00 (+14.88%)
- 確定: 2089件 (Win 610 / Loss 817 / Flat 662) / pending 0件 / skip 2659件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000246 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: FILECOIN/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $114.88

## 6. Latest Market Context

- 更新: 2026-09-01T22:46:16.590177+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.00% price=77179.9
- Funnel: target 1036 → liquid 161 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BONER/USDT:USDT | +19.96% | $2,123,471.34 |
| MAGMA/USDT:USDT | +19.39% | $2,996,199.66 |
| UAI/USDT:USDT | +16.94% | $14,207,146.93 |
| ACE/USDT:USDT | +12.69% | $8,352,364.48 |
| FONE/USDT:USDT | +10.63% | $1,288,360.33 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PONS/USDT:USDT | below_1h_threshold | +3.20% | +3.20% |
| CASHCAT/USDT:USDT | below_1h_threshold | +3.18% | +3.18% |
| NIULAI/USDT:USDT | below_1h_threshold | +2.02% | +2.02% |
| ACE/USDT:USDT | below_1h_threshold | +1.97% | +1.97% |
| EGLD/USDT:USDT | below_1h_threshold | +0.99% | +0.99% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
