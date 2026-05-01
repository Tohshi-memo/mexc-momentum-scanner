# Decision Report

- generated_at: 2026-05-01T21:56:59.252341+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2836**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.05% / filled 20/20。**
- 全期間 MARKET基準: n=2836, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+1.05%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.05% | **+1.05%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.54% | **+1.54%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.38% | **+1.32%** |
| MARKET | 20/20 | 100.0% | +1.05% | **+1.05%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +1.11% | **+0.83%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +0.74% | **+0.44%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +0.57% | **+0.37%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.39% | **+0.31%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +0.50% | **+0.25%** |

## 2. $100 Live Portfolio

- 残高: **$103.02** / 初期 $100.00 (+3.02%)
- 確定トレード: 6件 (TP 4 / SL 2 / EXP 0)
- 最新: RLS/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.02
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-01T21:56:57.261745+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.36% price=78117.2
- Funnel: target 755 → liquid 191 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +27.69% | $8,000,770.07 |
| CHILLGUY/USDT:USDT | +12.59% | $1,029,314.03 |
| RLS/USDT:USDT | +9.28% | $2,301,878.71 |
| BLESS/USDT:USDT | +8.80% | $1,023,769.32 |
| ZEN/USDT:USDT | +7.89% | $9,121,048.45 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CHILLGUY/USDT:USDT | below_1h_threshold | +3.66% | +3.30% |
| PLAY/USDT:USDT | below_1h_threshold | +3.26% | +2.90% |
| PHAROS/USDT:USDT | below_1h_threshold | +2.39% | +2.04% |
| TRB/USDT:USDT | below_1h_threshold | +2.27% | +1.91% |
| M/USDT:USDT | below_1h_threshold | +1.94% | +1.58% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
