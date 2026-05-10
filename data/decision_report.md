# Decision Report

- generated_at: 2026-05-10T17:15:39.831360+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3972**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3972, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=-1.74%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.74% | **-1.74%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +0.52% | **+0.05%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.02% | **+0.01%** |
| LIMIT_BB3S | 4/18 | 22.2% | -0.19% | **-0.04%** |
| LIMIT_3PCT | 16/20 | 80.0% | -0.52% | **-0.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +3.79% | **+1.71%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +2.09% | **+1.56%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +2.06% | **+1.24%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +2.61% | **+1.17%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +1.87% | **+0.94%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 30件 (TP 7 / SL 20 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$107.73** / 初期 $100.00 (+7.73%)
- 確定: 198件 (Win 48 / Loss 66 / Flat 84) / skip 335件
- 成長率目線: 平均log +0.000376 / 幾何平均 +0.038% per trade / maxDD +4.09%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BILL/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $107.73

## 4. Latest Market Context

- 更新: 2026-05-10T17:15:36.905011+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=81317.6
- Funnel: target 769 → liquid 159 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BASED/USDT:USDT | +6.10% | $2,596,713.81 |
| TRUTH/USDT:USDT | +5.92% | $1,556,363.61 |
| SUI/USDT:USDT | +5.68% | $425,308,692.46 |
| SEI/USDT:USDT | +5.07% | $31,498,571.62 |
| SAHARA/USDT:USDT | +4.88% | $4,045,331.42 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| APT/USDT:USDT | below_1h_threshold | +1.82% | +1.85% |
| SUI/USDT:USDT | below_1h_threshold | +1.57% | +1.60% |
| SAHARA/USDT:USDT | below_1h_threshold | +1.49% | +1.52% |
| INX/USDT:USDT | below_1h_threshold | +1.39% | +1.42% |
| XLM/USDT:USDT | below_1h_threshold | +1.18% | +1.21% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
