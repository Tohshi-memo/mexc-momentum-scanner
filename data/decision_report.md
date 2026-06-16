# Decision Report

- generated_at: 2026-06-16T06:12:51.226433+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6841**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6841, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.55%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.55% | **-1.55%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 3/20 | 15.0% | +5.87% | **+0.88%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.08% | **+0.38%** |
| LIMIT_FIB1272 | 11/20 | 55.0% | +0.44% | **+0.24%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_7PCT | 4/20 | 20.0% | +0.70% | **+0.14%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.18% | **+2.18%** |
| ASK_LONG | 20/20 | 100.0% | +1.96% | **+1.96%** |
| LIMIT_6PCT_LONG | 6/20 | 30.0% | +4.00% | **+1.20%** |
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +1.30% | **+0.84%** |
| LIMIT_5PCT_LONG | 6/20 | 30.0% | +2.14% | **+0.64%** |

## 2. $100 Live Portfolio

- 残高: **$102.50** / 初期 $100.00 (+2.50%)
- 確定トレード: 10件 (TP 5 / SL 5 / EXP 0)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.50
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$181.96** / 初期 $100.00 (+81.96%)
- 確定: 1714件 (Win 446 / Loss 534 / Flat 734) / skip 1688件
- 成長率目線: 平均log +0.000349 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ROAM/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $181.96

## 4. Robust Adaptive DryRun ($100)

- 残高: **$97.60** / 初期 $100.00 (-2.40%)
- 確定: 156件 (Win 28 / Loss 30 / Flat 98) / skip 96件
- 成長率目線: 平均log -0.000155 / 幾何平均 -0.016% per trade / maxDD +3.03%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0382 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $97.60

## 5. Latest Market Context

- 更新: 2026-06-16T06:12:47.065574+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.20% price=66159.8
- Funnel: target 777 → liquid 157 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ROAM/USDT:USDT | +62.44% | $3,512,435.95 |
| BSB/USDT:USDT | +29.55% | $20,966,822.69 |
| SPACE/USDT:USDT | +27.22% | $2,447,488.11 |
| ASTEROID/USDT:USDT | +26.25% | $5,394,475.85 |
| VELVET/USDT:USDT | +24.69% | $12,491,755.70 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VELVET/USDT:USDT | below_1h_threshold | +2.31% | +2.12% |
| ROAM/USDT:USDT | below_1h_threshold | +1.96% | +1.77% |
| ASTEROID/USDT:USDT | below_1h_threshold | +1.78% | +1.58% |
| SIREN/USDT:USDT | below_1h_threshold | +1.46% | +1.26% |
| UNI/USDT:USDT | below_1h_threshold | +1.17% | +0.97% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
