# Decision Report

- generated_at: 2026-06-22T23:29:49.727989+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7399**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7399, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_4PCT | 16/20 | 80.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1272 | 12/20 | 60.0% | -0.21% | **-0.12%** |
| LIMIT_BB3S | 6/20 | 30.0% | -1.81% | **-0.54%** |
| LIMIT_ATR | 15/20 | 75.0% | -0.75% | **-0.56%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +3.49% | **+1.92%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +2.19% | **+1.53%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.50% | **+1.27%** |
| MARKET_LONG | 20/20 | 100.0% | +1.20% | **+1.20%** |
| ASK_LONG | 20/20 | 100.0% | +1.12% | **+1.12%** |

## 2. $100 Live Portfolio

- 残高: **$101.94** / 初期 $100.00 (+1.94%)
- 確定トレード: 29件 (TP 11 / SL 18 / EXP 0)
- 最新: RE/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.94
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$236.22** / 初期 $100.00 (+136.22%)
- 確定: 2055件 (Win 611 / Loss 676 / Flat 768) / skip 1905件
- 成長率目線: 平均log +0.000418 / 幾何平均 +0.042% per trade / maxDD +7.25%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTW/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $236.22

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 313件 (Win 89 / Loss 87 / Flat 137) / skip 497件
- 成長率目線: 平均log +0.000187 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0022 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SYN/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-22T23:29:45.361524+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=64011.4
- Funnel: target 808 → liquid 158 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SYN/USDT:USDT | +19.21% | $29,780,726.17 |
| FOLKS/USDT:USDT | +18.64% | $2,180,016.91 |
| VELVET/USDT:USDT | +17.95% | $18,261,327.76 |
| UP/USDT:USDT | +15.16% | $1,011,778.69 |
| BLESS/USDT:USDT | +14.61% | $10,048,911.23 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTW/USDT:USDT | below_1h_threshold | +4.29% | +4.19% |
| TNSR/USDT:USDT | below_1h_threshold | +3.32% | +3.23% |
| VELVET/USDT:USDT | below_1h_threshold | +3.03% | +2.93% |
| UP/USDT:USDT | below_1h_threshold | +2.76% | +2.66% |
| FOLKS/USDT:USDT | below_1h_threshold | +1.86% | +1.77% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
