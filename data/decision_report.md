# Decision Report

- generated_at: 2026-05-02T07:17:06.542374+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2876**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2876, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_10PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_1PCT | 20/20 | 100.0% | +1.06% | **+1.06%** |
| LIMIT_BB3S | 7/19 | 36.8% | +2.46% | **+0.91%** |
| LIMIT_8PCT | 3/20 | 15.0% | +2.57% | **+0.39%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.52% | **+1.37%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.10% | **+0.82%** |
| MARKET_LONG | 20/20 | 100.0% | +0.40% | **+0.40%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +3.97% | **+0.40%** |
| ASK_LONG | 20/20 | 100.0% | +0.37% | **+0.37%** |

## 2. $100 Live Portfolio

- 残高: **$102.51** / 初期 $100.00 (+2.51%)
- 確定トレード: 7件 (TP 4 / SL 3 / EXP 0)
- 最新: BIO/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.51
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-02T07:17:04.817552+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=78262.6
- Funnel: target 755 → liquid 168 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +113.45% | $74,372,116.54 |
| IRYS/USDT:USDT | +19.77% | $1,271,869.16 |
| B/USDT:USDT | +16.13% | $78,972,536.67 |
| FIGHT/USDT:USDT | +12.59% | $1,092,887.51 |
| BLESS/USDT:USDT | +11.52% | $2,123,726.43 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PLAY/USDT:USDT | below_1h_threshold | +4.57% | +4.59% |
| BIO/USDT:USDT | below_1h_threshold | +2.12% | +2.14% |
| FIGHT/USDT:USDT | below_1h_threshold | +1.28% | +1.30% |
| IRYS/USDT:USDT | below_1h_threshold | +0.95% | +0.97% |
| BLESS/USDT:USDT | below_1h_threshold | +0.83% | +0.85% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
