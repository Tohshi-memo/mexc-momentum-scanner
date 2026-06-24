# Decision Report

- generated_at: 2026-06-24T07:55:51.375404+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7467**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7467, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 3/20 | 15.0% | +5.14% | **+0.77%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +2.37% | **+0.36%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.31% | **+1.12%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.10% | **+0.82%** |
| ASK_LONG | 20/20 | 100.0% | +0.81% | **+0.81%** |
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | -0.89% | **-0.09%** |

## 2. $100 Live Portfolio

- 残高: **$101.93** / 初期 $100.00 (+1.93%)
- 確定トレード: 32件 (TP 12 / SL 20 / EXP 0)
- 最新: ID/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.93
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$232.82** / 初期 $100.00 (+132.82%)
- 確定: 2098件 (Win 622 / Loss 695 / Flat 781) / skip 1930件
- 成長率目線: 平均log +0.000403 / 幾何平均 +0.040% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: G/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $232.82

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.55** / 初期 $100.00 (+7.55%)
- 確定: 330件 (Win 94 / Loss 88 / Flat 148) / skip 548件
- 成長率目線: 平均log +0.000221 / 幾何平均 +0.022% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0671 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: G/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +0.69% 残高後 $107.55

## 5. Latest Market Context

- 更新: 2026-06-24T07:55:44.140327+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.16% price=62653.9
- Funnel: target 807 → liquid 162 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +39.29% | $14,189,388.80 |
| SLX/USDT:USDT | +38.88% | $2,811,148.06 |
| BEAT/USDT:USDT | +30.36% | $84,310,494.86 |
| SAHARA/USDT:USDT | +16.60% | $1,462,596.60 |
| ID/USDT:USDT | +15.41% | $1,349,810.32 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PIPPIN/USDT:USDT | below_1h_threshold | +2.64% | +2.80% |
| GRAM/USDT:USDT | below_1h_threshold | +2.00% | +2.16% |
| SYN/USDT:USDT | below_1h_threshold | +1.97% | +2.13% |
| TERSTOCK/USDT:USDT | below_1h_threshold | +0.72% | +0.88% |
| ALLO/USDT:USDT | below_1h_threshold | +0.40% | +0.56% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
