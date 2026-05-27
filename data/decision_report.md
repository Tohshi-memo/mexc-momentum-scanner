# Decision Report

- generated_at: 2026-05-27T06:44:23.673101+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4922**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4922, expectancy=-0.08%
- 直近20件 MARKET基準: n=20, expectancy=-0.69%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.69% | **-0.69%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_4PCT | 12/20 | 60.0% | -0.33% | **-0.20%** |
| LIMIT_BB3S | 2/16 | 12.5% | -4.00% | **-0.50%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.57% | **+1.34%** |
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +1.77% | **+1.33%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +2.31% | **+1.04%** |
| MARKET_LONG | 20/20 | 100.0% | +0.92% | **+0.92%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +1.41% | **+0.70%** |

## 2. $100 Live Portfolio

- 残高: **$97.16** / 初期 $100.00 (-2.84%)
- 確定トレード: 65件 (TP 18 / SL 44 / EXP 3)
- 最新: ESPORTS/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.16
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$127.43** / 初期 $100.00 (+27.43%)
- 確定: 683件 (Win 172 / Loss 219 / Flat 292) / skip 800件
- 成長率目線: 平均log +0.000355 / 幾何平均 +0.035% per trade / maxDD +4.72%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PLAY/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $127.43

## 4. Latest Market Context

- 更新: 2026-05-27T06:44:21.492731+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.14% price=75779.2
- Funnel: target 772 → liquid 147 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PLAY/USDT:USDT | +22.77% | $10,835,085.92 |
| REQ/USDT:USDT | +19.16% | $1,532,412.55 |
| GUA/USDT:USDT | +11.50% | $3,903,401.11 |
| LUNC/USDT:USDT | +11.27% | $11,643,558.01 |
| ICP/USDT:USDT | +8.69% | $10,444,898.51 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GUA/USDT:USDT | below_1h_threshold | +3.85% | +3.71% |
| FILECOIN/USDT:USDT | below_1h_threshold | +2.04% | +1.90% |
| PLAY/USDT:USDT | below_1h_threshold | +1.86% | +1.72% |
| QNT/USDT:USDT | below_1h_threshold | +1.58% | +1.44% |
| INJ/USDT:USDT | below_1h_threshold | +1.48% | +1.35% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
