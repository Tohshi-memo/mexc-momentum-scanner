# Decision Report

- generated_at: 2026-05-12T12:11:58.687525+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4115**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4115, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=-1.34%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.34% | **-1.34%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_4PCT | 15/20 | 75.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | -0.37% | **-0.15%** |
| LIMIT_3PCT | 16/20 | 80.0% | -0.60% | **-0.48%** |
| LIMIT_2PCT | 17/20 | 85.0% | -0.91% | **-0.77%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +2.27% | **+1.59%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +2.51% | **+1.26%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.33% | **+1.13%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +1.92% | **+0.96%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +2.11% | **+0.95%** |

## 2. $100 Live Portfolio

- 残高: **$99.19** / 初期 $100.00 (-0.81%)
- 確定トレード: 34件 (TP 9 / SL 22 / EXP 3)
- 最新: DOGS/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.19
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$115.07** / 初期 $100.00 (+15.07%)
- 確定: 251件 (Win 69 / Loss 86 / Flat 96) / skip 425件
- 成長率目線: 平均log +0.000559 / 幾何平均 +0.056% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BILL/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.77% 残高後 $115.07

## 4. Latest Market Context

- 更新: 2026-05-12T12:11:55.190142+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=80800.6
- Funnel: target 763 → liquid 188 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SAGA/USDT:USDT | +50.14% | $15,987,795.94 |
| GIGA/USDT:USDT | +49.29% | $6,206,311.39 |
| SKYAI/USDT:USDT | +39.93% | $43,724,899.00 |
| GUA/USDT:USDT | +32.85% | $3,479,208.88 |
| USELESS/USDT:USDT | +31.44% | $9,024,457.30 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BILL/USDT:USDT | below_1h_threshold | +3.05% | +2.98% |
| INJ/USDT:USDT | below_1h_threshold | +1.76% | +1.69% |
| UB/USDT:USDT | below_1h_threshold | +1.53% | +1.46% |
| TRUTH/USDT:USDT | below_1h_threshold | +1.48% | +1.41% |
| GIGA/USDT:USDT | below_1h_threshold | +1.37% | +1.29% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
