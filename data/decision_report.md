# Decision Report

- generated_at: 2026-09-02T00:51:42.903555+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13282**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13282, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.11%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.11% | **-1.11%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 10/20 | 50.0% | +1.68% | **+0.84%** |
| LIMIT_8PCT | 5/20 | 25.0% | +3.02% | **+0.76%** |
| LIMIT_7PCT | 5/20 | 25.0% | +2.48% | **+0.62%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.08% | **+0.38%** |
| LIMIT_2PCT | 19/20 | 95.0% | +0.32% | **+0.30%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +4.27% | **+2.56%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +3.80% | **+1.90%** |
| LIMIT_2PCT_LONG | 19/20 | 95.0% | +1.73% | **+1.64%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +3.65% | **+1.46%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.99% | **+1.39%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 196件 (TP 73 / SL 118 / EXP 5)
- 最新: BTR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$827.97** / 初期 $100.00 (+727.97%)
- 確定: 4917件 (Win 1498 / Loss 1618 / Flat 1801) / skip 4926件
- 成長率目線: 平均log +0.000430 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FONE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $827.97

## 4. Robust Adaptive DryRun ($100)

- 残高: **$174.69** / 初期 $100.00 (+74.69%)
- 確定: 2261件 (Win 632 / Loss 544 / Flat 1085) / skip 4432件
- 成長率目線: 平均log +0.000247 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.0955 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: FONE/USDT:USDT `LIMIT_6PCT` SL_HIT account -0.35% 残高後 $174.69

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.88** / 初期 $100.00 (+14.88%)
- 確定: 2089件 (Win 610 / Loss 817 / Flat 662) / pending 0件 / skip 2665件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000373 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: FILECOIN/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $114.88

## 6. Latest Market Context

- 更新: 2026-09-02T00:51:24.920159+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.32% price=77156.1
- Funnel: target 1036 → liquid 162 → pre 50 → checked 50 → surge 3 → strict 3
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FONE/USDT:USDT | +38.14% | $1,359,790.75 |
| UAI/USDT:USDT | +24.89% | $16,770,317.67 |
| MAGMA/USDT:USDT | +19.58% | $4,429,768.07 |
| ACE/USDT:USDT | +14.97% | $10,189,024.42 |
| BONER/USDT:USDT | +10.85% | $2,383,456.90 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PYTH/USDT:USDT | below_1h_threshold | +2.90% | +3.22% |
| ZKP/USDT:USDT | below_1h_threshold | +1.82% | +2.13% |
| UAI/USDT:USDT | below_1h_threshold | +1.54% | +1.86% |
| DELLSTOCK/USDT:USDT | below_1h_threshold | +1.51% | +1.83% |
| AKE/USDT:USDT | below_1h_threshold | +1.36% | +1.68% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
