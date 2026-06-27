# Decision Report

- generated_at: 2026-06-27T10:56:31.267165+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7691**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7691, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.04%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.04% | **-0.04%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +5.45% | **+0.55%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.17% | **+0.35%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +0.87% | **+0.09%** |
| LIMIT_9PCT | 2/20 | 10.0% | +0.29% | **+0.03%** |
| LIMIT_BB3S | 2/17 | 11.8% | +0.05% | **+0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +1.50% | **+0.67%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +0.80% | **+0.40%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +2.53% | **+0.38%** |
| MARKET_LONG | 20/20 | 100.0% | +0.20% | **+0.20%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |

## 2. $100 Live Portfolio

- 残高: **$102.65** / 初期 $100.00 (+2.65%)
- 確定トレード: 41件 (TP 15 / SL 25 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.65
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$232.52** / 初期 $100.00 (+132.52%)
- 確定: 2216件 (Win 662 / Loss 739 / Flat 815) / skip 2036件
- 成長率目線: 平均log +0.000381 / 幾何平均 +0.038% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RE/USDT:USDT `LIMIT_FIB1272_LONG` SL_HIT account -0.50% 残高後 $232.52

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.04** / 初期 $100.00 (+7.04%)
- 確定: 422件 (Win 114 / Loss 107 / Flat 201) / skip 680件
- 成長率目線: 平均log +0.000161 / 幾何平均 +0.016% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0379 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $107.04

## 5. Latest Market Context

- 更新: 2026-06-27T10:56:25.479389+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=60364.9
- Funnel: target 806 → liquid 151 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +94.74% | $109,677,154.18 |
| MYX/USDT:USDT | +42.85% | $12,697,905.04 |
| SYRUP/USDT:USDT | +21.64% | $2,074,712.89 |
| PUNDIX/USDT:USDT | +18.04% | $6,370,509.43 |
| SLX/USDT:USDT | +13.91% | $9,934,927.44 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VELVET/USDT:USDT | below_1h_threshold | +2.74% | +2.79% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.15% | +2.20% |
| SYRUP/USDT:USDT | below_1h_threshold | +1.52% | +1.57% |
| AAVE/USDT:USDT | below_1h_threshold | +1.43% | +1.47% |
| SNT/USDT:USDT | below_1h_threshold | +1.41% | +1.45% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
