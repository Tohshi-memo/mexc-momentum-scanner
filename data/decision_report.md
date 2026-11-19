# Decision Report

- generated_at: 2026-11-19T22:56:17.252380+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19221**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19221, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.97%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.97% | **-1.97%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.16% | **+0.07%** |
| LIMIT_4PCT | 16/20 | 80.0% | -0.25% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +3.51% | **+1.58%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +3.08% | **+1.23%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +1.84% | **+0.92%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +2.11% | **+0.63%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.14% | **+0.63%** |

## 2. $100 Live Portfolio

- 残高: **$121.25** / 初期 $100.00 (+21.25%)
- 確定トレード: 282件 (TP 102 / SL 172 / EXP 8)
- 最新: KORU/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,692.99** / 初期 $100.00 (+1592.99%)
- 確定: 7381件 (Win 2119 / Loss 2376 / Flat 2886) / skip 8401件
- 成長率目線: 平均log +0.000383 / 幾何平均 +0.038% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ANTHROPIC/USDT:USDT `LIMIT_BB3S_LONG` SL_HIT account -0.50% 残高後 $1,692.99

## 4. Robust Adaptive DryRun ($100)

- 残高: **$439.03** / 初期 $100.00 (+339.03%)
- 確定: 5045件 (Win 1347 / Loss 1087 / Flat 2611) / skip 7587件
- 成長率目線: 平均log +0.000293 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0016 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: EVAA/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $439.03

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7380件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000231 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-19T22:56:05.890572+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +1.08% price=62179.8
- Funnel: target 1084 → liquid 151 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RARE/USDT:USDT | +20.81% | $1,999,010.89 |
| SKY/USDT:USDT | +14.09% | $4,685,882.49 |
| UVXY/USDT:USDT | +12.68% | $2,622,446.12 |
| SOXS/USDT:USDT | +12.57% | $47,656,849.24 |
| BLESS/USDT:USDT | +11.97% | $9,680,352.78 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EVAA/USDT:USDT | below_1h_threshold | +4.92% | +3.84% |
| ICNT/USDT:USDT | below_1h_threshold | +4.46% | +3.37% |
| HUMA/USDT:USDT | below_1h_threshold | +3.49% | +2.40% |
| AKE/USDT:USDT | below_1h_threshold | +3.12% | +2.03% |
| RARE/USDT:USDT | below_1h_threshold | +2.94% | +1.86% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
