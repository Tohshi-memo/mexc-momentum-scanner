# Decision Report

- generated_at: 2026-10-01T03:41:27.273411+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15868**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15868, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.33%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.33% | **-0.33%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_5PCT | 10/20 | 50.0% | +1.16% | **+0.58%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.05% | **+0.37%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.42% | **+0.30%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.60% | **+0.88%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +1.74% | **+0.87%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.45% | **+0.80%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.05% | **+0.53%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.44% | **+0.42%** |

## 2. $100 Live Portfolio

- 残高: **$120.75** / 初期 $100.00 (+20.75%)
- 確定トレード: 225件 (TP 82 / SL 136 / EXP 7)
- 最新: XLM/USDT:USDT SL_HIT PnL -2.52% 残高後 $120.75
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,215.00** / 初期 $100.00 (+1115.00%)
- 確定: 5990件 (Win 1766 / Loss 1927 / Flat 2297) / skip 6439件
- 成長率目線: 平均log +0.000417 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MOVR/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $1,215.00

## 4. Robust Adaptive DryRun ($100)

- 残高: **$263.08** / 初期 $100.00 (+163.08%)
- 確定: 3537件 (Win 974 / Loss 812 / Flat 1751) / skip 5742件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1002 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MOVR/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $263.08

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4030件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000206 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-01T03:41:15.826417+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.16% price=83576.2
- Funnel: target 1097 → liquid 172 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MOVR/USDT:USDT | +37.74% | $9,324,309.07 |
| MONAD/USDT:USDT | +16.11% | $4,939,517.72 |
| STX/USDT:USDT | +11.76% | $3,955,223.06 |
| NIGHT/USDT:USDT | +11.57% | $5,838,944.73 |
| BTW/USDT:USDT | +5.80% | $14,162,584.16 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| KORU/USDT:USDT | below_1h_threshold | +2.70% | +2.54% |
| LIT/USDT:USDT | below_1h_threshold | +2.54% | +2.39% |
| MARSCOIN/USDT:USDT | below_1h_threshold | +2.19% | +2.04% |
| ALGO/USDT:USDT | below_1h_threshold | +2.19% | +2.03% |
| BTW/USDT:USDT | below_1h_threshold | +2.14% | +1.98% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
