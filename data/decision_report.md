# Decision Report

- generated_at: 2026-09-18T19:16:31.069475+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14941**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14941, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.19%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.19% | **+0.19%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 3/20 | 15.0% | +1.96% | **+0.29%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.29% | **+0.25%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| MARKET | 20/20 | 100.0% | +0.19% | **+0.19%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.13% | **+0.04%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.85% | **+1.66%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +2.03% | **+1.63%** |
| MARKET_LONG | 20/20 | 100.0% | +1.09% | **+1.09%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.00% | **+0.65%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +1.26% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$120.56** / 初期 $100.00 (+20.56%)
- 確定トレード: 215件 (TP 79 / SL 131 / EXP 5)
- 最新: BULLA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.56
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,148.20** / 初期 $100.00 (+1048.20%)
- 確定: 5606件 (Win 1679 / Loss 1816 / Flat 2111) / skip 5896件
- 成長率目線: 平均log +0.000435 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EVAA/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,148.20

## 4. Robust Adaptive DryRun ($100)

- 残高: **$241.67** / 初期 $100.00 (+141.67%)
- 確定: 3173件 (Win 878 / Loss 757 / Flat 1538) / skip 5179件
- 成長率目線: 平均log +0.000278 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1791 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LONGXIA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $241.67

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.52** / 初期 $100.00 (+23.52%)
- 確定: 2962件 (Win 879 / Loss 1167 / Flat 916) / pending 0件 / skip 3453件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000534 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PIEVERSE/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.34% 残高後 $123.52

## 6. Latest Market Context

- 更新: 2026-09-18T19:16:20.297589+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.35% price=81188.3
- Funnel: target 1050 → liquid 169 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +48.22% | $17,174,903.98 |
| SAGA/USDT:USDT | +22.23% | $3,819,787.50 |
| USELESS/USDT:USDT | +14.84% | $7,131,053.66 |
| STRK/USDT:USDT | +14.50% | $5,401,453.81 |
| BR/USDT:USDT | +9.43% | $20,752,054.10 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STRK/USDT:USDT | below_1h_threshold | +3.72% | +3.37% |
| AERO/USDT:USDT | below_1h_threshold | +3.11% | +2.76% |
| SAGA/USDT:USDT | below_1h_threshold | +3.07% | +2.72% |
| SPX/USDT:USDT | below_1h_threshold | +2.43% | +2.08% |
| ZKSYNC/USDT:USDT | below_1h_threshold | +2.25% | +1.90% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
