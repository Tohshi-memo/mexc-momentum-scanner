# Decision Report

- generated_at: 2026-08-30T00:11:26.889790+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12975**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12975, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.40% | **-1.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 5/20 | 25.0% | +4.92% | **+1.23%** |
| LIMIT_8PCT | 5/20 | 25.0% | +3.88% | **+0.97%** |
| LIMIT_10PCT | 4/20 | 20.0% | +4.36% | **+0.87%** |
| LIMIT_7PCT | 9/20 | 45.0% | +1.69% | **+0.76%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +3.61% | **+3.25%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +4.14% | **+3.10%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +4.15% | **+2.90%** |
| MARKET_LONG | 20/20 | 100.0% | +1.01% | **+1.01%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +2.21% | **+0.99%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 194件 (TP 73 / SL 116 / EXP 5)
- 最新: SKR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$768.59** / 初期 $100.00 (+668.59%)
- 確定: 4745件 (Win 1444 / Loss 1558 / Flat 1743) / skip 4791件
- 成長率目線: 平均log +0.000430 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PONS/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $768.59

## 4. Robust Adaptive DryRun ($100)

- 残高: **$169.91** / 初期 $100.00 (+69.91%)
- 確定: 2059件 (Win 571 / Loss 494 / Flat 994) / skip 4327件
- 成長率目線: 平均log +0.000257 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1746 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PONS/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +0.69% 残高後 $169.91

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.05** / 初期 $100.00 (+15.05%)
- 確定: 2037件 (Win 597 / Loss 794 / Flat 646) / pending 0件 / skip 2411件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000457 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $115.05

## 6. Latest Market Context

- 更新: 2026-08-30T00:11:15.844881+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=78139.3
- Funnel: target 1023 → liquid 117 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI n/a=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FONE/USDT:USDT | +34.84% | $1,209,104.35 |
| PROM/USDT:USDT | +27.21% | $9,723,023.44 |
| PONS/USDT:USDT | +23.06% | $1,175,043.79 |
| HNT/USDT:USDT | +21.06% | $23,273,074.92 |
| BTR/USDT:USDT | +16.65% | $9,748,708.91 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PONS/USDT:USDT | below_1h_threshold | +3.35% | +3.43% |
| 4/USDT:USDT | below_1h_threshold | +2.74% | +2.81% |
| DOS/USDT:USDT | below_1h_threshold | +2.38% | +2.46% |
| BTW/USDT:USDT | below_1h_threshold | +1.50% | +1.57% |
| LONGXIA/USDT:USDT | below_1h_threshold | +1.23% | +1.31% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
